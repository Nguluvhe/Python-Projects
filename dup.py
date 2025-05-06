import pandas as pd

# Load the two CSV files
#df1 = pd.read_csv('data1.csv')  # e.g., columns: name, age
#df2 = pd.read_csv('data2.csv')  # e.g., columns: name, salary
df2 = pd.read_csv("/home/infbr003/Downloads/Titan_Pricefile_MV.csv")      # has ItemNumber
df1 = pd.read_csv("/home/infbr003/Downloads/sample_items.csv")

# Merge them on the 'name' column
merged_df = pd.merge(df1, df2, on='name', how='outer')  # use 'inner' or 'outer' as needed

# Save the merged DataFrame to a new CSV file
merged_df.to_csv('merged_output.csv', index=False)

print("CSV file created successfully: merged_output.csv")
