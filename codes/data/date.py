import pandas as pd
from datetime import datetime, timedelta

# Read the original CSV file
df = pd.read_csv("unique_clues.csv")

# Convert the 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Get the latest date in the dataset
latest_date = df['Date'].max()

# Calculate one year before the latest date
one_year_before = latest_date - timedelta(days=365)

# Filter the rows for Vlad within this date range
vlad_filtered = df[(df['Date'] >= one_year_before) & (df['Date'] <= latest_date)]

# Save to a new CSV file
vlad_filtered.to_csv("ast_year.csv", index=False)
