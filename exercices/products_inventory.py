"""Ejercicio: Inventario de Productos
Crea una clase Producto que represente un artículo en un inventario. Cada producto debe tener:
- nombre (str)
- precio (float)
- stock (int)
Requisitos:
- Los atributos deben estar encapsulados (privados).
- Implementa métodos para:
- Obtener y modificar el precio y el stock.
- Vender una cantidad de productos (disminuye el stock).
- Mostrar la información del producto.
- Si se intenta vender más productos de los que hay en stock, lanza una excepción personalizada StockInsuficienteError.
"""
class StockInsuficienteError(Exception):
    def __init__(self, mensaje="No hay suficiente stock para completar la venta."):
        super().__init__(mensaje)

class Product:
    def __init__(self, name: str, price: float, stock: int):
        self._name = name
        self._price = price
        self._stock = stock
        
    def get_price(self):
        return self._price

    def modify_price(self, new_price):
        self._price = new_price
        print(f'El producto {self._name} ha sido actualizado en su precio: ${self._price}')

    def check_stock(self):
        print(f'El stock de {self._name} es de: {self._stock}')

    def modify_stock(self, new_stock):
        if new_stock < 0:
            raise ValueError('El stock no puede ser negativo')
        self._stock = new_stock
        print(f'El stock modifica de {self._name} es: {self._stock}')

    def sell(self, cantidad):
        if cantidad > self._stock:
            raise StockInsuficienteError()
        self._stock = self._stock - cantidad
        print(f'Has vendido {cantidad} unidades de producto: {self._name}, el stock restante es: {self._stock}')

    def info(self):
        print(f'El producto {self._name} tiene un precio de: ${self._price}, y hay disponibles para la venta: {self._stock}')

computadora = Product('Computadora', 1500.0, 10)
            
print(computadora.get_price())
computadora.modify_price(1600)
computadora.check_stock()
computadora.modify_stock(20)
computadora.sell(20)
computadora.info()
