# Data Quality Report (before and after cleaning)

- Rows before: 8,297
- Rows after: 8,294
- Duplicate rows removed: 3
- Rows with negative amounts (kept and flagged): 383
- Validation checks passed: no missing values in subagency_acronym, current_amount and fiscal_year; fiscal_year between 2001 and 2021

## Missing values (percent)
| Column | Before | After |
|---|---|---|
| subagency_acronym | 4.0 | 0.0 |
| activity_start_date | 71.9 | 71.9 |
| activity_end_date | 70.8 | 70.8 |