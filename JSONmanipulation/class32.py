import json

json_path = './JSONmanipulation/products.json'

# Lectura del archivo
with open(json_path, mode='r') as file:
    products = json.load(file)

# Mostrar el contenido

for product in products:
    print(product)