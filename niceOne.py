import csv
import random
import os

def transform_titan_data(titan_file, sample_file, output_file):
    
    # Read sample data to extract default values
    sample_defaults = {}
    sample_data = []

    with open(sample_file, 'r', encoding='utf-8') as f:
        sample_reader = csv.DictReader(f)
        headers = sample_reader.fieldnames

        for row in sample_reader:
            sample_data.append(row)

    # Extract default values for each field from sample data so that the titan file doesn't have empty columns
    for field in headers:
        values = [item[field].strip() for item in sample_data if item.get(field, '').strip()]
        sample_defaults[field] = values[0] if values else ''

    # Define product type mapping based on category code
    def get_product_type(category_code):
        code = category_code.strip()
        if 'LIT' in code:
            return 'goods'
        elif any(x in code for x in ['CAB', 'ELE', 'CON']):
            return 'capital_goods'
        else:
            return 'service'  # default

    # Function to cycle through sample data values for variation
    def get_varied_default(field):
        values = [item[field].strip() for item in sample_data if item.get(field, '').strip()]
        if not values:
            return sample_defaults.get(field, '')
        return random.choice(values)

    # Read and transform titan data
    transformed_data = []

    with open(titan_file, 'r', encoding='utf-8') as f:
        titan_reader = csv.DictReader(f)

        for row in titan_reader:
            new_item = {}

            for field in headers:
                new_item[field] = get_varied_default(field)

                # Override with Titan-specific mappings
                if field == 'Item Name':
                    new_item[field] = row.get('Item Description', '').strip()
                elif field == 'SKU':
                    new_item[field] = row.get('ItemNumber', '').strip()
                elif field == 'Rate':
                    new_item[field] = row.get('Unit Price', '').strip()
                elif field == 'Description':
                    new_item[field] = row.get('Item Description', '').strip()
                elif field == 'Product Type':
                    new_item[field] = get_product_type(row.get('Category Code', ''))
                elif field == 'Purchase Rate':
                    new_item[field] = row.get('Purchase_Cost', '').strip() or new_item[field]
                elif field == 'Purchase Description':
                    new_item[field] = row.get('Item Description', '').strip()

            transformed_data.append(new_item)

    # Write the transformed data to a new CSV file
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(transformed_data)

    print(f"Transformation complete! Processed {len(transformed_data)} items.")
    print(f"Output written to {output_file}")

if __name__ == "__main__":
    # File paths
    titan_file = "/home/infbr003/Downloads/Titan_Pricefile_MV.csv"
    sample_file = "/home/infbr003/Downloads/sample_items.csv"
    output_file = "/home/infbr003/Downloads/output.csv"

    # Make sure input files exist
    for file_path in [titan_file, sample_file]:
        if not os.path.exists(file_path):
            print(f"Error: File not found - {file_path}")
            exit(1)

    # Run the transformation
    transform_titan_data(titan_file, sample_file, output_file)
