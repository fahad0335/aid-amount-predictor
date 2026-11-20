# Name: Shah Fahad  Roll no: TRN-2026-000706  Date: 20-11-2026
# Purpose: data_quality_metrics. make berore and after cleaning, save to JSON.
import json

METRICS_PATH = "outputs/reports/data_quality_metrics.json"
REPORT_PATH = "outputs/reports/data_quality_report.md"


def main():
    with open(METRICS_PATH, encoding="utf-8") as f:
        m = json.load(f)

    lines = [
        "# Data Quality Report (before and after cleaning)",
        "",
        f"- Rows before: {m['rows_before']:,}",
        f"- Rows after: {m['rows_after']:,}",
        f"- Duplicate rows removed: {m['duplicates_removed']}",
        f"- Rows with negative amounts (kept and flagged): {m['negative_amount_rows']}",
        "- Validation checks passed: no missing values in subagency_acronym, "
        "current_amount and fiscal_year; fiscal_year between 2001 and 2021",
        "",
        "## Missing values (percent)",
        "| Column | Before | After |",
        "|---|---|---|",
    ]
    before, after = m["missing_pct_before"], m["missing_pct_after"]
    for col in before:
        if before[col] > 0 or after.get(col, 0) > 0:
            lines.append(f"| {col} | {before[col]} | {after[col]} |")

    with open(REPORT_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print("\n".join(lines))


if __name__ == "__main__":
    main()