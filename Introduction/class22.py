try:
    divisor = int(input('Intresa un numero divisor: '))
    result = 100/divisor
    print(result)

except ValueError as e:
    print('El divisor es erroneo', e)


# JERARQUIAS 
def print_exception_hierarchy(exception_class, indent=0):
    print(' ' * indent + exception_class.__name__)
    for subclass in exception_class.__subclasses__():
        print_exception_hierarchy(subclass, indent + 4)

# Imprimir la jerarquía comenzando desde la clase base Exception
print_exception_hierarchy(Exception)
