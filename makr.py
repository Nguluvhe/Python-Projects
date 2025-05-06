import pandas as pd

# Load the CSV files
df2 = pd.read_csv("/home/infbr003/Downloads/Titan_Pricefile_MV (copy).csv")      # has ItemNumber
df1 = pd.read_csv("/home/infbr003/Downloads/sample_items (copy).csv")           # has SKU

# Ensure both merge keys are strings
df2["ItemNumber"] = df2["ItemNumber"].astype(str)
df1["SKU"] = df1["SKU"].astype(str)

# Corrected merge: match df1[SKU] with df2[ItemNumber]
merged_df = df1.merge(df2, how='outer')

# Save the merged result
merged_df.to_csv("/home/infbr003/Downloads/copymerged_output.csv", index=False)

print("Merged data saved to '/home/infbr003/Downloads/merged_output.csv'")
