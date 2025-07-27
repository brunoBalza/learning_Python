# Ejemplo de uso de iteradores en Python

lista = [1 , 2, 3, 4, 5, 6, 7, 8, 9, 10]

iterador = iter(lista)

print (iterador)

print(next(iterador))  # Imprime el primer elemento de la lista
print(next(iterador))  # Imprime el segundo elemento de la lista 
print(next(iterador))  # Imprime el tercer elemento de la lista

# Iterar en cadena de texto
cadena = "Hola Mundo"
iterador_cadena = iter(cadena)

    #Iteramos con ciclo for

for letra in iterador_cadena:
    print(letra)  # Imprime cada letra de la cadena "Hola Mundo"

# Iterar numero impares

limit = 10

odd_itter = iter(range(1, limit + 1, 2))
                 
for num in odd_itter:
    print(num)  # Imprime los números impares desde 1 hasta 10

# Generador

def my_generator():
    yield 1
    yield 2
    yield 3

for value in my_generator():
    print(value)  # Imprime 1, luego 2, luego 3


def fibonacci (limit):
    a, b = 0, 1
    while a< limit:
        yield a
        a, b = b, a+b

for num in fibonacci(50):
    print(num)