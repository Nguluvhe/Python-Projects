import csv

def to_sentence_case(text):
    """Converts a string to sentence case."""
    return text.capitalize() if isinstance(text, str) and text else text

# Mapping from file1 headers to output headers
header_mapping = {
    "ItemNumber": "SKU",
    "Item Description": "Item Name",
    "Unit Price": "Rate",
    "Category Code": "SKU",
    "Purchase_Cost": "Purchase Rate",
}

# Output headers (same as file2 format)
file2_headers = [
    "Item Name", "SKU", "Description", "Rate", "Product Type", "Account", "Usage unit",
    "Purchase Description", "Purchase Rate", "Item Type", "Purchase Account",
    "Inventory Account", "Reorder Point", "Vendor", "Initial Stock",
    "Initial Stock Rate", "Stock On Hand", "Status", "Tax Name", "Tax Type",
    "Tax Percentage", "Purchase Tax Name", "Purchase Tax Type",
    "Purchase Tax Percentage", "Warehouse Name", "CF.custom_field"
]

# Read file1.csv (tab-separated)
with open('/home/infbr003/Downloads/Titan_Pricefile_MV.csv', mode='r', newline='', encoding='utf-8') as f1:
    file1_reader = csv.DictReader(f1, delimiter='\t')
    file1_data = list(file1_reader)

# Read file2.csv (comma-separated, assumed format)
with open('/home/infbr003/Downloads/sample_items.csv', mode='r', newline='', encoding='utf-8') as f2:
    file2_reader = csv.DictReader(f2)
    file2_lookup = {row["SKU"]: row for row in file2_reader}  # Build a lookup by SKU

# Build combined output
output_rows = []

for row in file1_data:
    new_row = {}
    sku = row.get("ItemNumber", "").strip()
    file2_row = file2_lookup.get(sku, {})  # fallback to empty if SKU not found in file2

    for header in file2_headers:
        # Special handling for Description using sentence-case from Item Description
        if header == "Description" and "Item Description" in row:
            new_row[header] = to_sentence_case(row["Item Description"])
        # Map from file1 using header_mapping
        elif any(v == header for v in header_mapping.values()):
            source_key = next((k for k, v in header_mapping.items() if v == header), None)
            value = row.get(source_key, "")
            new_row[header] = value if value else file2_row.get(header, "")
        else:
            # If not in file1 mapping, get from file2
            new_row[header] = file2_row.get(header, "")

    output_rows.append(new_row)

# Write combined output
with open('/home/infbr003/Downloads/output.csv', mode='w', newline='', encoding='utf-8') as f_out:
    writer = csv.DictWriter(f_out, fieldnames=file2_headers)
    writer.writeheader()
    writer.writerows(output_rows)

print("Merged data from file1 and file2 written to 'output.csv'")
