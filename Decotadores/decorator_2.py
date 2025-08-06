def check_access(func):
    def wrapper(employee):
        #Comprobar si tiene acceso de "admin"
        if employee.get('role') == 'admin':
            return func(employee)
        else:
            print('ACCESO DENEGADO. Solo los admin pueden acceder.')
    return wrapper
        

@check_access
def delete_employee(employee):
    print(f'El empleado {employee["name"]}, ha sido eliminado')


admin = {'name': 'Bruno', 'role': 'admin'}
employee = {'name': 'Juan', 'role': 'employee'}

delete_employee(admin)    

