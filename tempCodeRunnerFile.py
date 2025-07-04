matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


transposed = [[row [i] for row in matriz] for i in range(len(matriz[0]))]

print(matriz)
# print(transposed)

transposed_1 = []
for i in range(3):
    transposed_row = []
    for row in matriz:
        transposed_row.append(row[i])
    transposed_1.append(transposed_row)