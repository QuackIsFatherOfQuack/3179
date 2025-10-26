import pandas as pd

# Read your data
df = pd.read_csv("arrivals_long.csv", encoding="latin1")  

# Convert "Month" to datetime
df["Month"] = pd.to_datetime(df["Month"], format="%b-%y")

# Extract the year
df["Year"] = df["Month"].dt.year

# Exclude year 2025
df = df[df["Year"] != 2025]

# Group by State and Year and sum arrivals
yearly = df.groupby(["State", "Year"], as_index=False)["Arrivals"].sum()

# Save to new CSV
yearly.to_csv("yearly_arrivals.csv", index=False)

# Print the first few rows to check
print(yearly.head())
