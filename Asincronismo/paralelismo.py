import multiprocessing

#Funcion que calcule le cuadrado de un nuevo
def calculate_square(n):
    return n*n

if __name__ == '__main__':
    numbers = [1,2,3,4,5]

    #Crear pool
    with multiprocessing.Pool() as pool:
        result = pool.map(calculate_square, numbers)

    print(f'Resultados: {result}')