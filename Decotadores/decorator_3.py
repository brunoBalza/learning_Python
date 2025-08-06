def check_access(required_role):
    def decorator(func):
        def wrapper(employee):
            if employee.get('role') == required_role:
                return func(employee)
            else:
                print(f'ACCESS Denied, {employee["name"]}, is not admin')
        return wrapper
    return decorator

def log_action(func):
    def wrapper(employee):
        print(f'Registrando accion para el empleado: {employee["name"]}')
        return func(employee)
    return wrapper


@log_action
@check_access('admin')
def delete_employee(employee):
    print(f'El empleado {employee["name"]}, ha sido eliminado')

admin = {'name': 'Bruno', 'role': 'admin'}
employee = {'name': 'Juan', 'role': 'employee'}

delete_employee(employee)