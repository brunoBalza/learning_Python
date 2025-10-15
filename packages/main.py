#Importar archivos desde la carpeta "packages"
from ecommerce.inventory import add_product, remove_product
from ecommerce.sales import process_sale


add_product('Laptop', 100)
remove_product('Laptop')
process_sale('Laptop', 5)

def f(x): return x * 2 print(f(3))
    

