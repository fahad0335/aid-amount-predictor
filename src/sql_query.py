# Name: Shah Fahad  Roll no: TRN-2026-000706  Date: 19-11-2026
# Purpose:save clean data to SQLite database and run SQL query to get aid by type, save result to CSV.
import sqlite3
import pandas as pd

CLEAN_PATH = "data/cleaned/us_aid_cleaned.csv"
DB_PATH = "data/cleaned/us_aid.db"
SQL_PATH = "sql/aid_by_type.sql"
RESULT_PATH = "outputs/reports/sql_aid_by_type.csv"


def main():
    df = pd.read_csv(CLEAN_PATH, low_memory=False)

    conn = sqlite3.connect(DB_PATH)
    df.to_sql("aid", conn, if_exists="replace", index=False)

    with open(SQL_PATH, encoding="utf-8") as f:
        query = f.read()

    result = pd.read_sql_query(query, conn)
    conn.close()

    result.to_csv(RESULT_PATH, index=False)
    print(result.to_string(index=False))


if __name__ == "__main__":
    main()
