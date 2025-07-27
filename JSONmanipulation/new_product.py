import json

json_path = './JSONmanipulation/products.json'

new_product = {
    'name': 'Milanesas',
    'price': '8',
    'quantity': '10',
    'brand': 'Bru-Car',
    'category': 'Food',
    'entry_date': '2024-01-05'
}

# Primero abro el archivo en modo lectura

with open(json_path, mode='r') as file:
    products = json.load(file)

products.append(new_product)

with open(json_path, mode='w') as file:
    json.dump(products, file, indent=4)