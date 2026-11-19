# Name: Shah Fahad
# Roll no: TRN-2026-000706
# Date: 19-11-2026
import pandas as pd

PATH = "data/raw/us_aid_pakistan.csv"
df = pd.read_csv(PATH, low_memory=False)

# 1. Size aur column types
print("Shape (rows, columns):", df.shape)
print(df.dtypes)

# 2. Missing values in percentage
print((df.isna().mean() * 100).round(1).sort_values(ascending=False))

# 3. Duplicate rows
print("Duplicates:", df.duplicated().sum())

#checking the targeted column status
print(df["current_amount"].describe())
print("Negative amounts:", (df["current_amount"] < 0).sum())
print("Zero amounts:", (df["current_amount"] == 0).sum())

# checking the unique values in each column
print(df.nunique())