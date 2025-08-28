# Ejercicio 8
# Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división entera respectivamente.

n = int(input("Ingresá el primer número (dividendo): "))
m = int(input("Ingresá el segundo número (divisor): "))


if n > m :
    raise ValueError('El dividendo no puede ser meñor que el divisor')
# Calcular cociente y resto
else:
    c = n // m
    r = n % m
    print(f"La {n} entre {m} da un cociente {c} y un resto {r}")