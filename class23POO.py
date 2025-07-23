class Person:
    def __init__(self, name, age):  
        self.name = name
        self.age = age

    def greet (self):
        print(f'Hola, no nombre es {self.name} y tengo {self.age}')

person1 = Person("Bruno", 34)
person2 = Person('Rocio', 35)

person1.greet()
person2.greet()