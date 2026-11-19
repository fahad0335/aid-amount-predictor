# Name: Shah Fahad  Roll no: TRN-2026-000706  Date: 19-11-2026
# Purpose: making markdown table for schema of the dataset, and checking allowed values for some categorical columns
import pandas as pd

PATH = "data/raw/us_aid_pakistan.csv"
df = pd.read_csv(PATH, low_memory=False)


lines = [
    "| Column | Type | Missing count | Missing % | Unique values | Example |",
    "|---|---|---|---|---|---|",
]

# one line for each column
for col in df.columns:
    missing = df[col].isna().sum()
    pct = round(missing / len(df) * 100, 1)
    example = str(df[col].dropna().iloc[0])[:30].replace("|", "/")
    lines.append(
        f"| {col} | {df[col].dtype} | {missing} | {pct} | {df[col].nunique()} | {example} |"
    )

# save the file in outputs/reports/schema_table.md
with open("outputs/reports/schema_table.md", "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

# small check for allowed values in some categorical columns
for col in ["assistance_category_name", "aid_type_group_name", "channel_category_name"]:
    print(col, "->", sorted(df[col].unique()))

print("fiscal_year range:", df["fiscal_year"].min(), "to", df["fiscal_year"].max())
