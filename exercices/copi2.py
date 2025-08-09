class Pizza:
    base_price = 4000

    def __init__(self, ingredientes: list[str], tamanio: str):
        self.ingredientes = ingredientes
        self.tamanio = tamanio

    def precio_total(self) -> int:
        
        if self.tamanio == 'mediana':
            return self.base_price + 500 + len(self.ingredientes) * 100
        if self.tamanio == 'grande':
            return self.base_price + 1000 + len(self.ingredientes) * 100
        if self.tamanio == 'chica':
           return self.base_price + len(self.ingredientes) * 100
        else:
            print('El tamaño ingresado no es correcto!')

pizza = Pizza(['Muzzarella', 'Tomate', 'Ajo'], 'grande')

print(pizza.ingredientes)
print(pizza.precio_total())


#  Resultado mejor

class Pizza:
    base_price = 4000
    ingrediente_price = 150
    tamanio_extra = {
        'chica': 0,
        'mediana': 500,
        'grande': 1000
    }

    def __init__(self, ingredientes: list[str], tamanio: str):
        self.ingredientes = ingredientes
        self.tamanio = tamanio.lower()  # Por si viene en mayúsculas

        if self.tamanio not in self.tamanio_extra:
            raise ValueError(f"Tamaño inválido: '{self.tamanio}'. Debe ser chica, mediana o grande.")

    def precio_total(self) -> int:
        extra = self.tamanio_extra[self.tamanio]
        ingredientes_total = len(self.ingredientes) * self.ingrediente_price
        return self.base_price + extra + ingredientes_total


# Ejemplo de uso
pizza = Pizza(['Muzzarella', 'Tomate', 'Ajo'], 'Grande')

print("Ingredientes:", pizza.ingredientes)
print("Precio total: $", pizza.precio_total())
