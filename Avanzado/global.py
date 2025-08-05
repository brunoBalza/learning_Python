x = 5

def modify_global():
    global x
    x+=3
    print(f'La variable ahora modificada es {x}')

modify_global()
print(x)