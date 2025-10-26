import pandas as pd

# This is transforming State-arrival to long format
#----------------------------------------------------------------------
# df = pd.read_csv("data/State-arrival-residence.csv", encoding="latin1")  

# # Transform from wide to long
# df_long = df.melt(
#     id_vars=["Month"],
#     var_name="State",
#     value_name="Arrivals"
# )

# # Save new CSV (use UTF-8 for safety)
# df_long.to_csv("arrivals_long.csv", index=False, encoding="utf-8")

# # Print first few rows to confirm
# print(df_long.head(10))
#----------------------------------------------------------------------

#Transform for data viz 2
# #----------------------------------------------------------------------
# df = pd.read_csv("Arrival_by_citizenship.csv", encoding="latin1")

# # Reshape to long format
# df_long = df.melt(id_vars=["Month"], var_name="Country", value_name="Value")

# # Remove 4 digits
# df_long["Country"] = df_long["Country"].str.replace(r"^\s*\d{4}\s*", "", regex=True)

# # Convert values to numeric
# df_long["Value"] = pd.to_numeric(df_long["Value"], errors="coerce")

# # Compute total per country
# country_totals = df_long.groupby("Country")["Value"].sum()

# # Get countries with total >= 10,000
# valid_countries = country_totals[country_totals >= 10000].index

# # Filter dataset
# df_filtered = df_long[df_long["Country"].isin(valid_countries)]
# df_filtered = df_filtered[df_filtered["Country"] != "Australia"]

# df_filtered.to_csv("citizenship_arrival.csv", index=False)

# print("Original countries:", df_long["Country"].nunique())
# print("Remaining countries:", df_filtered["Country"].nunique())
# #----------------------------------------------------------------------

# Transform for data viz 3
#----------------------------------------------------------------------
# df = pd.read_csv("citizenship_arrival.csv")

# # Convert Month to datetime (assuming format like "Jan-1991")
# df["Month"] = pd.to_datetime(df["Month"], format="%b-%Y")

# # Keep last 15 years
# df_recent = df[df["Month"] >= "2010-01-01"]

# # Compute total arrivals by month (excluding Australia)
# monthly = df_recent.groupby("Month")["Value"].sum().reset_index()
# monthly.rename(columns={"Value": "VisitorArrivals"}, inplace=True)

# # Calculate pre-COVID baseline (e.g., average from 2010–2019)
# baseline = monthly[(monthly["Month"] >= "2010-01-01") & (monthly["Month"] < "2020-01-01")]["VisitorArrivals"].mean()
# print("Pre-COVID baseline:", round(baseline))

# # Save for Vega-Lite
# # monthly.to_csv("tourism_trend.csv", index=False)
# print(monthly.head(10))
#----------------------------------------------------------------------

# Transform for data viz 4
#----------------------------------------------------------------------
# df = pd.read_csv("Short-terms-reasons.csv", encoding="latin1")  

# df_long = df.melt(
#     id_vars=["Month"],  
#     var_name="Purpose",                  
#     value_name="Count"                   
# )

# df_long.to_csv("Visit_reasons_long.csv", index=False, encoding="utf-8")
# print(df_long.head(10))
#----------------------------------------------------------------------

# Transform for data viz 5
#----------------------------------------------------------------------
# df = pd.read_csv("Arrival_by_citizenship.csv")

# # Clean column names (optional)
# df.columns = df.columns.str.strip()

# # Convert Month to datetime for filtering
# df["Date"] = pd.to_datetime(df["Month"], format="%b-%Y", errors="coerce")

# # Calculate total visitors excluding Australia
# df["TotalVisitorCount"] = df["Total"] - df["1101 Australia"]

# # Filter from Jan 2015 onwards 
# df = df[df["Date"] >= "2015-01-01"]
# df = df[df["Date"] <= "2025-01-01"]

# # Keep only Month and TotalVisitorCount
# df_result = df[["Month", "TotalVisitorCount"]]

# # Save filtered data
# df_result.to_csv("Viz5_data.csv", index=False, encoding="utf-8")

#----------------------------------------------------------------------

# Transform for data viz 6
#----------------------------------------------------------------------
df = pd.read_csv("Short-terms-duration.csv")

# Convert Month column to datetime (assuming format like 'Jan-1991')
df["Month"] = pd.to_datetime(df["Month"], format="%b-%Y")

# Filter for data from 2015 onwards
df = df[df["Month"].dt.year >= 2015]

# Convert to long format
df_long = df.melt(
    id_vars=["Month"],
    var_name="Duration",
    value_name="VisitorCount"
)

# Preview
print(df_long.head())

# Save to new CSV
df_long.to_csv("Viz6_long_duration_visitors.csv", index=False)

#----------------------------------------------------------------------

# Transform for data viz 7
#----------------------------------------------------------------------

#----------------------------------------------------------------------