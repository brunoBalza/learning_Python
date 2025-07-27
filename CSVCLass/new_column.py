import csv

file_path = './CSVCLass/products.csv'
update_file_path = './CSVCLass/products_updates.csv'

with open(file_path, mode='r') as file:
    csv_reader = csv.DictReader(file)
    #Obetener los nombres de las columnas

    fieldnames = csv_reader.fieldnames + ['total_value']

    with open(update_file_path, mode='w', newline='') as updates_file:

        csv_writer = csv.DictWriter(updates_file, fieldnames=fieldnames)
        csv_writer.writeheader()

        for row in csv_reader:
            row['total_value'] = float(row['price']) * int(row['quantity'])
            csv_writer.writerow(row)