# Código lento y poco eficiente
numeros = [1, 2, 3, 4, 5]

cuadrados = []
for numero in numeros:
    cuadrados.append(numero ** 2)

# Código Pytónico usando list comprehension
cuadrados1 = [numero ** 2 for numero in numeros]