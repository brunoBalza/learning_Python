"""
Vas a crear una clase Bebida que representa una bebida vendida en un kiosco. Cada bebida tiene:
- nombre: nombre de la bebida (ej. "Coca-Cola")
- tamaño: puede ser 'chica', 'mediana' o 'grande'
- precio_base: precio sin importar el tamaño
- con_azucar: booleano que indica si tiene azúcar
Reglas de precio:
- 'chica': sin recargo
- 'mediana': +10%
- 'grande': +20%
- Si tiene azúcar, se suma un recargo fijo de $5

- Crear la clase con atributos privados.
- Implementar un método calcular_precio() que devuelva el precio final.
- Agregar un método descripcion() que devuelva un string como:
- "Coca-Cola grande con azúcar - Precio final: $XXX"

"""

class Bebida:

    def __init__(self, nombre, precio_base, tamaño, con_azucar):
        self.__nombre = nombre
        self.__tamaño = tamaño.lower()
        self.__precio_base = precio_base
        self.__con_azucar = con_azucar

    def calculated_price(self):
        
        recargo_tamaño = 0
        if self.__tamaño == 'mediana':
            recargo_tamaño = self.__precio_base * 0.1
        elif self.__tamaño == 'grande':
            recargo_tamaño = self.__precio_base * 0.2

        recargo_azucar = 5 if self.__con_azucar else 0

        return self.__precio_base + recargo_azucar + recargo_tamaño
    
    def descripcion(self):
        azucar_texto = "con azucar" if self.__con_azucar else "sin azucar"
        print(f'{self.__nombre} {self.__tamaño} {self.__con_azucar} - Precio final: {self.calculated_price()}')



        # return self._price * self._size + [5 for self._zugar in range(1) if True]

secco = Bebida('secco', 100, 'grande', True)
coca = Bebida('Coca', 100, 'mediana', True)
birrita = Bebida('Coca', 100, 'chica', True)

secco.descripcion()
coca.descripcion()
birrita.descripcion()