import asyncio #Perimite asincronismo
import time #Simula el tiempo de espera
import random #Simular diferentes tiempos de espera
import multiprocessing #Permite la concurrencia

#Creamos una funcion asincronia para verificar el inventario, entrada y servicio de base de datos

async def check_inventory(item):
    print(f'Verificando inventario para {item}...')
    await asyncio.sleep(random.randint(3,6)) #Va a darnos un tiempo de espera
    print(f'Inventario verificado para {item}')
    #Simular disponibilidad del producto
    return random.choice([True, False])

#Función asíncrona para procesar el pago

async def process_payment(order_id):
    print(f'Procensando pago para la orden: {order_id}...')
    #Simular tiempo de espera
    await asyncio.sleep(random.randint(3,6))
    print(f'Pago: {order_id}, procesado')
    return True

#Función intensiva de CPU para calcular el costo total del pedido
def calculate_total(items):
    print(f'Calculando el costo total para: {len(items)} artículos...')
    time.sleep(5)
    total = sum(item['price'] for item in items)
    print(f'Costo toal calculado: {total}')
    return total

#Función que nos va a ayudar a procesar la orden
async def process_order(order_id, items):
    print(f'Iniciando el procesamiento de la orden: {order_id}...')
    #Verificar el inventario de forma asincrona de cada artículo
    invetory_checks = [check_inventory(item['name']) for item in items]
    inventory_result = await asyncio.gather(*invetory_checks)

    if not all(inventory_result):
        print(f'Orden {order_id}, Cancelada. Producto no disponible')
    
    with multiprocessing.Pool() as pool:
        total = pool.apply(calculate_total, (items,)) #La coma al final es para iterar

    #Procesar el pago de forma asíncrona
    payment_result = await process_payment(order_id)

    if payment_result:
        print(f'Orden {order_id} completa con éxito. Total: {total}')

    else: 
        print(f'Error al procesar el pago de la orden: {order_id}')

async def main():
    orders = [
        {'order_id': 1, 'items': [{'name': 'Laptop', 'price': 1000}, {'name': 'Mouse', 'price': 50}]},
        {'order_id': 2, 'items': [{'name': 'Teclado', 'price': 80}, {'name': 'Monitor', 'price': 300}]},
        {'order_id': 3, 'items': [{'name': 'Smartphone', 'price': 700}, {'name': 'Funda', 'price': 20}]}
    ]

    #Procesar multiples ordenes concurrentes
    tasks = [process_order(order['order_id'], order['items']) for order in orders]
    #Establemos una pausa
    await asyncio.gather(*tasks) #Que todas las tareas se realicen de forma simultenea

#Creamos el EvenLoop para procesar todas las ordenes

if __name__ == '__main__':
    asyncio.run(main())