# Factoriales

def factorial(n):
    if n == 0:
        return 1

    else:
        return n * factorial(n-1)

result = factorial(5)       
print(result)

# Fibo

def fibo (n):
    if n == 0:
        return "No es posible"
    else:
        return n + fibo(n-1)

result1 = fibo(10)       
print(result1)

# Sumatoria de numeros naturales

def sumatoria(n):
    if n == 0:
        return 0

    else:
        return n + sumatoria(n-1)

print(sumatoria(10))