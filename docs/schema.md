# Raw Data Schema

## Source
- Dataset: US Aid to Pakistan (2001-2021)
- Source URL: https://opendata.com.pk/dataset/us-aid-to-pakistan
- Licence: The licence was locked only avalible to the those people who has login access
- Access date: 19-11-2026
- Rows: 8,297    Columns: 21

## Units, formats and allowed values
- current_amount unit: ... (source page ya data dictionary se confirm karna hai)
- fiscal_year: whole numbers from 2001 to 2021 (21 values)
- activity_start_date / activity_end_date: text in the format `YYYY-MM-DD 00:00:00 UTC`. In the non-missing rows the time part is always `00:00:00 UTC`, so only the date matters. Observed start dates range from 1988-05-23 to 2017-12-30.
- assistance_category_name: Economic, Military
- aid_type_group_name: Administrative Costs, Budget support, Core contributions, Debt relief, Project-Type, Technical Assistance
- channel_category_name: Church and Faith Based, Enterprises, Government, Multilateral, NGO, Public and Private Partnerships, Universities and Research Institutes

## Missing values observed
- activity_start_date: 71.9% missing (5,966 rows). activity_end_date: 70.8% missing (5,874 rows).
- The dates are filled much more often in later years (about 2% of rows in 2002, about 40% in 2016-2018), so the missing dates look related to when the record was made. This is an observation from the data, not a confirmed reason.
- subagency_acronym: 4.0% missing (329 rows).

## Other observations
- 3 fully duplicated rows.
- current_amount: 383 negative values, 0 zero values.
- subagency_acronym has 43 unique values but subagency_name has 45. To be checked during cleaning.

## Column table

| Column | Type | Missing count | Missing % | Unique values | Example |
|---|---|---|---|---|---|
| implementing_agency_acronym | str | 0 | 0.0 | 16 | USAID |
| implementing_agency_name | str | 0 | 0.0 | 16 | U.S. Agency for International  |
| subagency_acronym | str | 329 | 4.0 | 43 | ASIA |
| subagency_name | str | 0 | 0.0 | 45 | Bureau for Asia |
| channel_category_name | str | 0 | 0.0 | 7 | Government |
| channel_subcategory_name | str | 0 | 0.0 | 16 | Government - Non United States |
| channel_name | str | 0 | 0.0 | 365 | Government of Pakistan |
| dac_category_name | str | 0 | 0.0 | 10 | Humanitarian |
| dac_sector_name | str | 0 | 0.0 | 30 | Emergency Response |
| dac_purpose_name | str | 0 | 0.0 | 92 | Material relief assistance and |
| funding_account_name | str | 0 | 0.0 | 58 | Economic Support Fund |
| assistance_category_name | str | 0 | 0.0 | 2 | Economic |
| activity_name | str | 0 | 0.0 | 1166 | Pakistan Emergency Economic As |
| activity_start_date | str | 5966 | 71.9 | 302 | 2001-11-16 00:00:00 UTC |
| activity_end_date | str | 5874 | 70.8 | 244 | 2001-11-16 00:00:00 UTC |
| fiscal_year | int64 | 0 | 0.0 | 21 | 2002 |
| current_amount | int64 | 0 | 0.0 | 7295 | 600000000 |
| funding_agency_name | str | 0 | 0.0 | 15 | U.S. Agency for International  |
| funding_agency_acronym | str | 0 | 0.0 | 15 | USAID |
| aid_type_group_name | str | 0 | 0.0 | 6 | Budget support |
| activity_description | str | 0 | 0.0 | 1378 | Pakistan Emergency Economic As |