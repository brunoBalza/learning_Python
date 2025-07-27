import csv

# Leer un archivo CSV

with open('./CSVCLass/products.csv', mode='r') as file:
    csv_reader = csv.DictReader(file) # Aca le decimos que queremos el archivo en lectura de modo diccionario
    for row in csv_reader:
        print(f'Producto: {row["name"]} - $ {row["price"]}')
