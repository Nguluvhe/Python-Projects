#Use the pandas module
import pandas as pd

df1 = pd.read_csv("F:\Project\Python\sample_items.csv", encoding="utf-8")
df2 = pd.read_csv("F:\Project\Python\Titan_Pricefile_MV.csv", encoding="utf-8")

#template for mapping the columns
column_map = {
    "ItemNumber": "SKU",
    "Item Description": "Item Name",
    "Category Code": "Product Type",
    "Purchase_Cost": "Purchase Rate"
}

#rename the columns using the map template
df2_rename = df2.rename(columns=column_map)

merge_df = pd.concat([df1, df2_rename], ignore_index=True)

merge_df.to_csv("F:\Project\Python\merge_csv.csv", index=False, encoding="utf-8")

