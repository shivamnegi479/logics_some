import pandas as pd

# Read the first CSV file
df1 = pd.read_csv('data.csv')

# Read the second CSV file
df2 = pd.read_csv('data2.csv')

# Merge the dataframes based on matching ID, person name, and age
merged_df = pd.merge(df1, df2, on=['City', 'Name', 'Age'], how='outer')

# Forward fill missing values from the second dataframe to the first dataframe
merged_df['ID_x'].fillna(merged_df['ID_y'], inplace=True)
merged_df['ID_y'].fillna(merged_df['ID_x'], inplace=True)
# merged_df.drop(['City_y', 'ID_y'], axis=1, inplace=True)
# merged_df.rename(columns={'City_x': 'City', 'ID_x': 'ID'}, inplace=True)
print(merged_df)
# Save the merged dataframe to a new CSV file
# merged_df.to_csv('merged.csv', index=False)
