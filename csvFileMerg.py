#Use the pandas module
import pandas as pd

df1 = pd.read_csv("F:\Project\Python\sample_items.csv", encoding="utf-8")
df2 = pd.read_csv("F:\Project\Python\Titan_Pricefile_MV.csv", encoding="utf-8")

#template for columns
column_map = {
    "ItemNumber": "SKU",
    "Item Description": "Item Name",
    "Category Code": "Product Type",
    "Purchase_Cost": "Purchase Rate"
}
column_drop = ["Discount", "Actual_Margin", "TitanSellingPrice", "LastPriceUpdate"]

#rename the columns using the map template
df2_rename = df2.rename(columns=column_map)

#Dropping the columns i don't need before merging and added errors ignore so that it ignores error if column doesn't exist
df2 = df2.drop(columns=column_drop, errors="ignore")

#Merging the data and added the ignore_index so that the two files don't have they own index
merge_df = pd.concat([df1, df2_rename], ignore_index=True)

#For filling data when the cell is empty the ffill fills data with the forward data and bfill uses the backward data 
merge_df = merge_df.fillna(method="ffill").fillna("bfill")

merge_df.to_csv("F:\Project\Python\merge_csv.csv", index=False, encoding="utf-8")

