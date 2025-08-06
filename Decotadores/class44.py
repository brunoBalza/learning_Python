def log_transaction(func):
    def wrapper():
        print('Log de la transacción...')
        func()
        print('Log terminado...')
    return wrapper

@log_transaction
def process_payment():
    print('Procesando pago...')

process_payment()