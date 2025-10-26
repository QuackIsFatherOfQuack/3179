import os

import pandas as pd

path = "data/citizenship_arrival.csv"
print("File found:", os.path.exists(path))

df = pd.read_csv("data/citizenship_arrival.csv")
bad_months = df[~df["Month"].str.match(r"^[A-Za-z]{3}-\d{4}$", na=False)]
print("Malformed Month entries:\n", bad_months)

bad_values = df[pd.to_numeric(df["Value"], errors="coerce").isna()]
print("Non-numeric or missing Value entries:\n", bad_values)

print("Unique sample of Country names:")
print(df["Country"].dropna().unique()[:10])

print("Rows with any missing value:")
print(df[df.isna().any(axis=1)])

df["Date"] = pd.to_datetime(df["Month"] + "-01", format="%b-%Y-%d", errors="coerce")
print(df["Date"].min(), "to", df["Date"].max())