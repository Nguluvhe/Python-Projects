#Use the pandas module
import pandas as pd

df1 = pd.read_csv("F:\Project\Python\sample_items.csv", encoding="utf-8")
df2 = pd.read_csv("F:\Project\Python\Titan_Pricefile_MV.csv", encoding="utf-8")

column_map = {
    "ItemNumber": "SKU",
    "Item Description": "Item Name",
    "Category Code": "Product Type",
    "Purchase_Cost": "Purchase Rate"
}

df2_rename = df2.rename(columns=column_map)




