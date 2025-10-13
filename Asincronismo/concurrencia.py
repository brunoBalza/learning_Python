import threading
import time

#funcion que simula el procesamiento de una solicitud
def process_request(request_id):
    print(f'Procesando solicitud {request_id}')
    time.sleep(3)
    print(f'Solicitud {request_id} completada')

threads = []

for i in range(3):
    #Crear un nuevo hilo que ajecutará la funcion
    thread = threading.Thread(target=process_request, args=(i,))
    threads.append(thread)
    thread.start()

for thread in threads:
    #Asegurar que el programa espera que cada hilo termine
    thread.join()

print('Todas las solicitudes completadas')