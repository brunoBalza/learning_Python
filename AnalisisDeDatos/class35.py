import statistics
import csv

monthly_sales = {}
ventas_path = './AnalisisDeDatos/ventas.csv'

with open(ventas_path, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        month = row['month']
        sales = int(row['sales'])
        monthly_sales[month] = sales

sales = list(monthly_sales.values())
print(sales)

# Hallar la media

mean_sales = statistics.mean(sales)
print(f'La media de las ventas es: {mean_sales}')

# Hallar la mediana 

median_sales = statistics.median(sales)
print(f'La mediana de las ventas es: ', median_sales)

# Hallar la moda

mode_sales = statistics.mode(sales)
print(f'La moda de las ventas es: ', mode_sales)

# Hallar la Desviacion estandar
stdev_sales = statistics.stdev(sales)
print(f'La Desviacion de las ventas es: ', stdev_sales)

# Hallar la varianza

variance_sales = statistics.variance(sales)
print(f'La varianza de las ventas es: {variance_sales}')

# Maximo y Minimo de ventas

max_sales = max(sales)
min_sales = min(sales)
print(f'El maximo de ventas es: {max_sales} y el minimo es: {min_sales}')

# Rango de ventas

range_sales = max_sales - min_sales
print(f'El rango de ventas es: {range_sales}')