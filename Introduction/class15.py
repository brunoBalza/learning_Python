x = 3
y = 11
if x > 5:
    print("x es mayor")
elif x < 5:
    print("x es menor")
else:
    print("x es cinco")

print("------")

if x > 5 and x < 10:
    print("x es mayor que 5 y y es menor que 10")
elif x < 5:
    print("x es menor que 5")
else : 
    print("y es mayor que 10")

print("------")

if x > 5 and y < 10:
    print("X Y estan en rango")
elif x < 5  and y < 10:
    print("X sale del rango")
elif x > 5 and y > 10:
    print("Y sale del rango")
else:   
    print("X Y salen del rango")

print("------")

if not x > 5:
    print("Negacion de que X sea mayor que 5")  
else:
    print("X es mayor que 5")