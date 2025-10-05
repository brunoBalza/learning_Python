def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multi(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ValueError("No puede dividir entre 0")
    return a / b

if __name__ == "__main__":
    print('Operaciones')
    res_1 = suma(2, 3)
    print(f'Suma: {res_1}')