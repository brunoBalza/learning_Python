add = lambda a, b: (a+2) + b
print(add(10, 2))

multiply = lambda a,b : a*b
print(multiply(2, 2))

#Cuadrados

numbers = list(range(11))
cuadrados = list(map(lambda x: x**2, numbers))
print(cuadrados)

#Pares

even_numbers = list(filter(lambda x: x%2 == 0, numbers))
print(even_numbers)