import pandas as pd

# Load data
df = pd.read_csv("yearly_arrivals.csv")

# Make sure Year is numeric
df['Year'] = pd.to_numeric(df['Year'], errors='coerce')

# For each state, find first and last year
first_last = (
    df.sort_values(['State', 'Year'])
      .groupby('State')
      .agg(start_year=('Year', 'first'),
           end_year=('Year', 'last'),
           start=('Arrivals', 'first'),
           end=('Arrivals', 'last'),
           min=('Arrivals', 'min'),
           max=('Arrivals', 'max'))
      .reset_index()
)

# Calculate growth
first_last['growth_%'] = ((first_last['end'] - first_last['start']) / first_last['start']) * 100

# Find overall min and max across all states
overall_min = df['Arrivals'].min()
overall_max = df['Arrivals'].max()
# Round for readability
print(first_last[['State', 'min', 'max', 'growth_%']].round(2))
print(f"Minimum arrivals: {overall_min:,.0f}")
print(f"Maximum arrivals: {overall_max:,.0f}")
