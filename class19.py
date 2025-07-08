
# saludo = "Hola"

# def saludar(palabra, palabra1="no alcanzaron a escribir"):
#     print(palabra, palabra1)

# saludar(saludo)

# a = 2 
# b = 3

# def math(a, b):
#     return a+b

# resultado = math(a, b)
# print(resultado)


def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

def calculator():
    while True:
        print("Seleccione una operacion")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicacion")
        print("4. Division")
        print("5. Salir")

        opcion = int(input("Ingrese su opcion [1,2,3,4,5]"))

        if opcion == 5:
            print('Saliste')
            break

        elif opcion in [1, 2, 3, 4] :
            num1 = float(input("Elija un numero del 1 al 10"))
            num2 = float(input("Elija otro numero del 1 al 10"))

            if opcion == 1:
                print("resultado es:", suma(num1, num2))
            elif opcion == 2:
                print("resultado es:", resta(num1, num2))
            elif opcion == 3:
                print("resultado es:", multiplicar(num1, num2))
            elif opcion == 4:
                print("resultado es:", dividir(num1, num2))
        else:
            return print('Opcion no válida')
    
calculator()