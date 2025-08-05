class Employee:
    name: str
    age: int
    salary: float

    def __init__(self, name: str, age: int, salary: float):
        self.name = name
        self.age = age
        self.salary = salary

    def introduce(self) -> str:
        return f"Hola mi nombre es {self.name}, tengo {self.age}, cobro {self.salary}"
    
employee1 = Employee("Bruno", "hola", 120)
print(employee1.introduce())