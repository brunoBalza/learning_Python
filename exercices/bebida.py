"""🧃 
Ejercicio: Clase Bebida
Objetivo: Crear una clase  que represente una bebida con ciertas propiedades y comportamientos.
🧩 Requisitos:
1. 	Atributos:
• 	 (str): el nombre de la bebida.
• 	 (list): lista de ingredientes.
• 	 (bool): indica si la bebida contiene alcohol.
• 	 (float): precio de la bebida.
2. 	Métodos:
• 	: inicializa los atributos.
• 	: agrega un ingrediente a la lista.
• 	: devuelve  si la bebida no es alcohólica y tiene menos de 4 ingredientes.
• 	: imprime la información completa de la bebida de forma legible.
3. 	Extras opcionales:
• 	Validar que el precio no sea negativo.
• 	Encapsular atributos sensibles como  usando propiedades ().
• 	Crear una subclase  que tenga un atributo adicional  y un método ."""

class Bebida:

    def __init__(self, nombre: str, ingredientes: list[str], alcoholica: bool, precio: float):
        self.nombre = nombre
        self.ingredientes = ingredientes
        self.alcoholica = alcoholica
        self._precio = precio

    @property
    def price(self):
        if self._precio < 0:
            raise ValueError('El valor ingresado no puede ser negativo')
        else:
            return self._precio

    def agregar_ingrediente(self, ingrediente: str):
        self.ingredientes.append(ingrediente)

    def es_saludable(self) -> bool:
        return not self.alcoholica and len(self.ingredientes) < 4
        

    def info(self):
        saludable_texto = 'es saludable' if self.es_saludable() else 'es alcoholica'
        print(f'La bebida: {self.nombre}, ingredientes: {self.ingredientes}, {saludable_texto}, - Precio: {self.price}')

class BebidaEspecial(Bebida):
    
    def __init__(self, nombre, ingredientes, alcoholica, precio, popularidad: int):
        super().__init__(nombre, ingredientes, alcoholica, precio)
        self.popularidad = popularidad

    def recomendar(self):
        if 8 <= self.popularidad <= 10:
            print('Muy recomendada')
        elif 4 <= self.popularidad <= 7:
            print('Recomendada')
        elif 0 <= self.popularidad <= 3:
            print('No recomendada')

        else:
            raise ValueError('Debe ingresar un valor entre 0 y 10 en popularidad')



    


# coca = Bebida('coca', ['azucar', 'coso1'], True, 100)

coca_light = BebidaEspecial('coca', ['azucar', 'coso1'], True, 100, 7)
coca_light.info()
# coca.info()
coca_light.recomendar()