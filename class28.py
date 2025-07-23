class LivingBeing:
    def __init__(self, name):
        self.name = name

class Person(LivingBeing):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def greet(self):
        print(f'Hello! I am a person, and my name is {self.name}')

class Student (Person):
    
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def greet(self):
        super().greet()
        print(f'Hello! I am a student, my name is {self.name}')

# person = Person('Bruno', 34)
student = Student('Bruno', 34, '123')

student.greet()