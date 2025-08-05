# Acá la variable no es local ni global

def outer_function():
    x = 'enclosing'

    def inner_function():
        nonlocal x
        x = 'modified'
        print (f'El valor de x es : {x}')

    inner_function()
    print(f'Acá el valor de x es: {x}')

outer_function()