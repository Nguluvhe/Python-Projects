import csv
import requests

ACCESS_TOKEN = 'your_oauth_token'
ORG_ID = '714608640'
BASE_URL = 'https://www.zohoapis.com/inventory/v1/items'

HEADERS = {
    'Authorization': f'Zoho-oauthtoken {ACCESS_TOKEN}',
    'Content-Type': 'application/json'
}

def update_item(row):
    item_id = row['ItemNumber']
    url = f'{BASE_URL}/{item_id}?organization_id={ORG_ID}'
    
    data = {
        "item_Name": None,
        "sku": None,
        "description": row['Item Description'],
        "rate": None,
        "product_type": None,
        "account": None,
        "usage_rate": None,
        "purchase_description": None,
        "purchase_rate": None,
        "item_type": None,
        "purchase_account": None,
        "inventory_account": None,
        "reorder_point": None,
        "vendor": None,
        "initial_stock": None,
        "initial_stock_rate": None,
        "stock_on_hand": None,
        "Status": None,
        "tax_name": None,
        "tax_type": None,
        "tax_type": None,
        "tax_percentage": None,
        "purchase_tax_name": None,
        "purchase_tax_type": None,
        "purchase_tax_percentage": None,
        "warehouse_name": None,
        "custom_fields": None
    }

    response = requests.put(url, json=data, headers=HEADERS)
    print(f"Item {item_id} update status: {response.status_code}")
    print(response.json())

with open('/home/infbr003/Downloads/Titan_Pricefile_MV.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        update_item(row)
