import csv

new_product = {
    'name': 'Milanesas',
    'price': '8',
    'quantity': '10',
    'brand': 'Bru-Car',
    'category': 'Food',
    'entry_date': '2024-01-05'
}

with open('./CSVCLass/products.csv', mode='a', newline='') as file:
    file.write('\n')
    csv_write = csv.DictWriter(file, fieldnames= new_product.keys())
    csv_write.writerow(new_product)