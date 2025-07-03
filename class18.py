squares = [x**2 for x in range(0,11)]

print(squares)

evens = [x for x in range(1,20) if x%2 == 0]

print(evens)

# Matriz y Traspuesta

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transposed = [[row [i] for row in matriz] for i in range(len(matriz[0]))]

print(matriz)
print(transposed)