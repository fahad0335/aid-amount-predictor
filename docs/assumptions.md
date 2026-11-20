# Assumptions, Limitations and Decisions

## Cleaning decisions
| Problem | What I did | Why |
|---|---|---|
| 3 duplicate rows | Removed them (8,297 -> 8,294 rows) | Exact copies would be counted twice and inflate totals and counts. |
| Date columns stored as text | Converted to datetime; unreadable values become missing | Text dates cannot be sorted, compared or used for year calculations. |
| activity_start_date 71.9% and activity_end_date 70.8% missing | Left missing, did not fill | Guessing dates for about 70% of rows would invent information. |
| subagency_acronym about 4% missing (329 rows) | Filled with "Unknown" | Keeps the rows. subagency_name is complete, so no real information is lost. |
| 383 negative current_amount values | Kept them and added a True/False column is_negative_amount | Deleting them would change the totals. The flag lets me include or exclude them later. |

## What I chose not to fix
- Very large amounts (maximum 600,000,000, median 85,000): kept. The largest record is a named emergency assistance activity, so it looks like a real large payment, not a typing error.
- subagency_acronym has 43 unique values but subagency_name has 45: not investigated yet, because it does not affect the analysis so far. To check later.
- Categories such as dac_purpose_name and channel_name have many values and were not merged or simplified.

## Assumptions
- Each row is one aid record, and fiscal_year is the year the record belongs to.
- The unit of current_amount is not confirmed from the source yet. The charts label it US dollars, which must be checked.
- Negative amounts probably are corrections or reductions, but the source has not confirmed this.

## Limitations
- Most activity dates are missing, so any analysis by activity date is not reliable. Analysis uses fiscal_year instead.
- Totals include negative amounts, so they are net amounts.
- Amounts are very skewed (a few very large records), so averages are misleading. The median is a better summary.
- The data has only one source and no way to check it against another.


## Leakage check (columns not used as features)
| Column | Decision | Reason |
|---|---|---|
| current_amount | Target | This is what we predict |
| is_negative_amount | Removed | Built from the target, so it would give the answer away |
| activity_name, activity_description | Removed | Free text, identical in 31% of rows, and may hint at the amount |
| *_acronym columns | Removed | Copies of the *_name columns |
| funding_agency_* | Removed | Same as the implementing agency in about 90% of rows |
| activity_start_date, activity_end_date | Removed | More than 70% missing |
| channel_name, dac_purpose_name | Not used | 365 and 92 categories, too many for this size of data |

# Model Card

## Problem
- Task: regression. Predict the size of a US aid record (`current_amount`).
- Target: log10 of `current_amount`. Predictions are converted back to US dollars.
- Rows used: 7,911 rows with a positive amount. The 383 negative rows were left out because the log of a negative number does not exist.

## Data and split
- Source: US Aid to Pakistan 2001-2021 (see docs/schema.md).
- Split by fiscal year: 2001-2017 for training (6,560 rows) and 2018-2021 for testing (1,351 rows).
- Why: the model would be used on future years, so a time-based split tests it the way it would really be used. A random split would mix old and new records and look better than it really is.
- Splitting happened before any fitting. The test set was used only once at the end, to produce the results table.

## Features
Agency, subagency, channel category, aid category, sector, funding account, assistance category (economic or military), aid type group and fiscal year.

## Pipeline
One scikit-learn Pipeline object: missing values filled, text categories one-hot encoded, fiscal_year scaled, then the model. It is fitted on the training data only. Unseen categories are ignored instead of crashing.

## Results (test set, log10 scale)
| Model | CV MAE | Test MAE | Test RMSE | Test R2 |
|---|---|---|---|---|
| Baseline (median) | 1.017 | 1.007 | 1.312 | -0.012 |
| Ridge | 0.878 | 0.833 | 1.116 | 0.267 |
| Random Forest | 1.305 | 0.792 | 1.078 | 0.316 |

- Metrics: MAE and RMSE show the size of the error and R2 shows how much better the model is than just guessing the average. Accuracy does not apply to a regression problem.
- Random Forest is the best on the test set, but only a little better than Ridge. A typical prediction is still about 6 times too high or too low.
- The cross-validation score of Random Forest is poor because the first folds are trained on very few early-year records.
- The saved pipeline is `outputs/models/aid_amount_pipeline.joblib`. `python -m src.predict` scores new rows from a CSV.

## Error analysis
- The biggest errors are on tiny records. Several rows with real amounts of 1, 14 or 34 dollars were predicted as hundreds of thousands. The model learns typical aid records and cannot recognise symbolic or adjustment entries.
- The error grows with time: the average error was 0.715 in 2018 and 0.981 in 2021, so the model gets weaker on later years.
- Military (16 test rows), budget support (1 row) and core contributions (3 rows) have too few test rows to judge reliably.
- The residual plot is centred near zero but widely spread, with a few very large over-predictions for tiny amounts.

## Intended use
- Learning and exploration: a rough guess of the size of an aid record from its agency, sector and type.

## Limitations
- R2 is about 0.3, so the features explain only a part of the amount.
- Negative records were excluded and are not predicted.
- Only one dataset from one source. The unit of current_amount is not confirmed from the source (assumed US dollars).
- Very small and very large amounts are predicted poorly.

## Risks
- It must not be used to decide real aid budgets or to judge any agency or project. A wrong guess could look more reliable than it is.
- Performance drops on later years, so it should not be trusted far into the future.
- The data records money amounts only, not results or need, so the model learns past spending patterns and may repeat them.
- The licence on the source page was not visible without login. The TA confirmed on 20-11-2026 that the dataset can be used for this assignment.