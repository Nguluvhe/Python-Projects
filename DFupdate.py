import pandas as pd

# Load the CSV files
df2 = pd.read_csv("/home/infbr003/Downloads/Titan_Pricefile_MV.csv")      # has ItemNumber
df1 = pd.read_csv("/home/infbr003/Downloads/sample_items.csv")           # has SKU

# Concatenate all rows from both DataFrames, keeping all columns
merged_df = pd.concat([df2, df1], axis=0, ignore_index=True, sort=False)

# Save the merged result
merged_df.to_csv("/home/infbr003/Downloads/merged_output.csv", index=False)

print("Merged data saved to '/home/infbr003/Downloads/merged_output.csv'")
