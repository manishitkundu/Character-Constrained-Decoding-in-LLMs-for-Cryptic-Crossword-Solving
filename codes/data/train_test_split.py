import pandas as pd
from sklearn.model_selection import train_test_split

# Read the original CSV file
df = pd.read_csv("unique_clues_filtered.csv")


# Convert Date column to datetime and extract the year
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df['Year'] = df['Date'].dt.year

# Function to split data for each (Author, Year) group
def split_group(group):
    if len(group) < 10:  # If the group is too small, assign everything to training
        return group.assign(Split='train')
    
    train, temp = train_test_split(group, test_size=0.2, random_state=42)  # 20% goes to test+val
    val, test = train_test_split(temp, test_size=0.5, random_state=42)  # Split remaining 10% each

    train['Split'] = 'train'
    val['Split'] = 'val'
    test['Split'] = 'test'

    return pd.concat([train, val, test])

# Apply the function to each (Author, Year) group
df_split = df.groupby(['Author', 'Year'], group_keys=False).apply(split_group)

# Save separate files for train, validation, and test splits
train_data = df_split[df_split['Split'] == 'train']
val_data = df_split[df_split['Split'] == 'val']
test_data = df_split[df_split['Split'] == 'test']

# Save to CSV
train_data.to_csv("unique_clues_train.csv", index=False)
val_data.to_csv("unique_clues_val.csv", index=False)
test_data.to_csv("unique_clues_test.csv", index=False)
