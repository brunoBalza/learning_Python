# Listas

to_do = ["Estudiar", 
         "Hacer ejercicio", 
         "Leer un libro"]

print(to_do)

number = [1, 
          2, 
          3,
          4,
          "five"]   

print(len(number)) # Imprime la longitud de la lista number

mix = [1, 
       "dos", 
       3.0,
       True,
       [1, 2, 3]]

print(mix)

print(mix[0])  # Imprime el primer elemento de la lista
print(mix[-1])  # Imprime el ultimo elemento de la lista

print(mix[1]) # Imprime los elementos desde el indice 2 hasta el 4 (5 no incluido)
print(mix[1:2])

# Añadir un elemento al final de la lista
mix.append(False)
print(mix)

# Añadir un elemento en una posición específica
mix.insert(2, "tres")
print(mix)

numbers = [1, 2, 3.5, 90, 100]
print(max(numbers))
print(min(numbers))

# Eliminar un elemento de la lista
del numbers[-1]
print(numbers)

del numbers[0:2]
print(numbers)

# Eliminar lista completa
del numbers
# print(numbers)  # Esto generará un error porque la lista ya no existe