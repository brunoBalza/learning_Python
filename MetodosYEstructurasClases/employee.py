class Employee:
    def __init__(self, name, *args, **kwargs):
        self.name = name
        self.skills = args
        self.detail = kwargs

    def show_employee(self):
        print(f'Employee: {self.name}')
        print(f'Skills: {self.skills}')
        print(f'Detail: {self.detail}')

employee1 = Employee('Bruno','Python, SQL, Postgres', city= 'Mendoza', age= 34)

employee1.show_employee()