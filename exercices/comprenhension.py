"""
🐣 Nivel 1: Básicos
- Números al cuadrado
Generá una lista con los cuadrados de los números del 1 al 10.
- Solo pares
Filtrá los números pares del 0 al 20.
- Longitudes de palabras
Dada una lista de palabras, creá una nueva lista con la longitud de cada palabra.
palabras = ["python", "copi", "lista", "comprehension"]
"""

squares = [a**2 for a in range(1, 11)]
# print(squares)

pairs = [a for a in range(1,21) if a%2 == 0]
# print(pairs)

palabras = ["python", "copi", "lista", "comprehension"]
length = [len(a) for a in palabras]
# print(length)

"""
🧠 Nivel 2: Transformaciones
- Mayúsculas selectivas
Convertí a mayúsculas solo las palabras que tengan más de 5 letras.
- Multiplicación condicional
Multiplicá por 2 los números impares del 1 al 15.
- Filtrar y limpiar
Dada una lista con strings que pueden tener espacios, devolvé una lista con los strings limpios (sin espacios) y que no estén vacíos.
sucios = ["  hola ", " ", "copi", "   ", "python  "]
"""

palabras = ["python", "copi", "lista", "comprehension", "hola", "si"]
mayusculas = [msj.upper() for msj in palabras if len(msj) > 5]
# print(mayusculas)

multi = [x*2 for x in range(1,16) if not x%2 == 0]
# print(multi)

sucios = ["  hola ", " ", "copi", "   ", "python  "]
limpio = [str.strip() for str in sucios if str.strip()]
# print(limpio)

"""
🧩 Nivel 3: Combinaciones y anidamientos- Producto cartesiano
Dadas dos listas, generá una lista con todos los pares posibles (x, y).
colores = ["rojo", "verde"]
formas = ["círculo", "cuadrado"]
- Matrices planas
Aplaná una matriz 2D en una sola lista.
matriz = [[1, 2], [3, 4], [5, 6]]
- Filtrar múltiplos en matriz
Dada una matriz de números, devolvé una lista con todos los múltiplos de 3.
"""
colores = ["rojo", "verde"]
formas = ["círculo", "cuadrado"]
pares = [(x, y) for x in formas for y in colores ]
# print(pares)

matriz = [[1, 2], [3, 4], [5, 6]]
dosd = [elemento for fila in matriz for elemento in fila]
# print(dosd)

multiplo = [elemento for fila in matriz for elemento in fila if elemento%3 == 0]
# print(multiplo)

"""
🧪 Nivel 4: Desafío Copi- Diccionario invertido con comprensión
Dado un diccionario, invertí las claves y valores usando una dict comprehension.
original = {"a": 1, "b": 2, "c": 3}
- List comprehension con if-else
Generá una lista que diga "par" o "impar" según el valor de cada número del 1 al 10.
- Extraer vocales de una frase
Dada una frase, devolvé una lista con todas las vocales que aparecen.
"""



original = {"a": 1, "b": 2, "c": 3}
convertir = {valor: clave for clave, valor in original.items()}
# original.items() te da una lista de tuplas [("a", 1), ("b", 2), ("c", 3)]
# En la comprensión, clave y valor se invierten: el nuevo diccionario tiene los valores como claves y las claves como valores.
# print(convertir)

resultado = ["par" if num % 2 == 0 else "impar" for num in range(1, 11)]
# if-else va adelante del for
# print(resultado)

frase = "Automatizá tu lógica con Python"
vocales = [letra for letra in frase if letra.lower() in "aeiou"]
# letra.lower convierte todo a minúscula
# le paso las vocales para que devuelva solamente esas letras
# print(vocales)

"""________________________________________________"""

# 1. Contador de palabras únicas

frase = "Python es poderoso y Python es divertido"
# .set() elimina repeticiones
# list() agrega la frase a una lista
resultado = list(set(frase.lower().split()))

print(resultado)
