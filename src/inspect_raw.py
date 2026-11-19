# Name: ...  Roll no: ...  Date: 19-11-2026
# Purpose: raw data ko sirf parhna aur dekhna. Kuch change ya save nahi karna.
import pandas as pd

PATH = "data/raw/us_aid_pakistan.csv"
df = pd.read_csv(PATH, low_memory=False)

# 1. Size aur column types
print("Shape (rows, columns):", df.shape)
print(df.dtypes)

# 2. Missing values, percent mein, sab se zyada upar
print((df.isna().mean() * 100).round(1).sort_values(ascending=False))

# 3. Duplicate rows
print("Duplicates:", df.duplicated().sum())

# 4. Target column current_amount ka haal
print(df["current_amount"].describe())
print("Negative amounts:", (df["current_amount"] < 0).sum())
print("Zero amounts:", (df["current_amount"] == 0).sum())

# 5. Har column mein kitni alag values hain
print(df.nunique())