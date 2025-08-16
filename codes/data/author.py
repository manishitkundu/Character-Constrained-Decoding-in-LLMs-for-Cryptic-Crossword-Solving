import pandas as pd

# Read the original CSV file
df = pd.read_csv("unique_clues.csv")

# Filter rows where Author is Vlad
vlad_rows = df[df['Author'] == 'Vlad']

# Write them to a CSV file named vlad.csv
vlad_rows.to_csv("vlad.csv", index=False)
