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

# Remove the filtered Vlad rows from the original dataset
df_filtered_out = df[~((df['Author'] == 'Vlad') | (df['Date'] >= one_year_before) & (df['Date'] <= latest_date))]

# Save the updated dataset back to CSV
df_filtered_out.to_csv("unique_clues_filtered.csv", index=False)
