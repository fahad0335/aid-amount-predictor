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