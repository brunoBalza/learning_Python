def divide(a: int, b: int) -> float:

    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError ('Aambos parametros deben ser enteros')
        
    if b == 0:
        raise ValueError('El divisor no puede ser 0')


    return a / b


# divide(5,0)
# divide(5,'0')
# print(divide(5,3))

try:
    res = divide(3, '2')
    print(res)
except TypeError as e:
    print(f'Error: {e}')    

try:
    res = divide(3, 0)
    print(res)
except ValueError as e:
    print(f'Error: {e}')   

try:
    res = divide(10,2)
    print(res)
except (TypeError, ValueError) as e:
    print(f'Error: {e}')  