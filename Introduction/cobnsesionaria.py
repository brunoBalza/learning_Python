class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.available = True

    def test(self):
        if self.available:
            self.available = False
            print(f'El automovil {self.model} esta en testeo')
        else:
            print(f'Este auto no esta disponible para testo')
    
    def return_test (self):
        self.available = True
        print(f'Auto: {self.model} ha sido devuelto del test')

    def sell(self):
        if self.available:
            self.available = False
            print(f'El automovil {self.model} ha sido vendido')
        else:
            print(f'Este auto no esta disponible para la venta')

    def ckeck_available (self):
        if self.available:
            return self.available
        
    def get_price (self):
        return self.price

class Client:
    def __init__(self, name, client_id):
        self.name = name
        self.client_id = client_id
        self.tested_cars = []
        self.cars_purchased = []

    def tested_car (self, car):
        if car.available:
            car.test()
            self.tested_cars.append(car)
        else:
            print(f'Este auto no esta disponible para testeo')
        
    def return_car (self, car):
        if car in self.tested_cars:
            car.return_test()
            self.tested_cars.remove(car)
        else:
            print(f'El auto {car.model} no esta en la lista de testeos')

    def buy_car (self, car):
        if car.ckeck_available():
            car.sell()
            self.cars_purchased.append(car)
        else:
            print(f'El auto {car.brand} {car.model} no esta disponible.')

    def inquire_car(self, car):
            availability = "disponible" if car.ckeck_available() else "no disponible"
            print(f"El coche {car.brand} {car.model} está {availability} y cuesta {car.get_price()}.")

class Dealership:
    def __init__ (self):
        self.clients = []
        self.cars= []

    def add_car (self, car):
        self.cars.append(car)
        print(f'El auto {car.model} ha sido agregado a la concesionaria')

    def register_client (self, client):
        self.clients.append(client)
        print(f'El cliente {client.name} ha sido registrado con exito!')
    
    def show_available_cars(self):
        print(f'Los autos disponibles son: ')
        for car in self.cars:
            if car.available:
                print(f'{car.brand} {car.model}')



# Creacion de autos

Auto1 = Car('Ford', 'Ka', 2000)
Auto2 = Car('Fiat', 'Cronos', 3000)
Auto3 = Car('BMW', '185', 5000)

# Registrar clientes

cliente1 = Client('Bruno', '001')
cliente2 = Client('Rocio', '002')
cliente3 = Client('Lair', '003')

# Creamos una concesionaria
 
Autoconnect = Dealership()

# Agregar autos a la concesionario

Autoconnect.add_car(Auto1)
Autoconnect.add_car(Auto2)
Autoconnect.add_car(Auto3)

# Agregar los clientes a la concesionaria

Autoconnect.register_client(cliente1)
Autoconnect.register_client(cliente2)
Autoconnect.register_client(cliente3)

# Prestamos una auto

cliente1.tested_car(Auto1)

# Cliente compra un auto

cliente2.buy_car(Auto2)

#Cliente consulta auto

cliente3.inquire_car(Auto3)

# Cliente intenta comprar un coche ya vendido

cliente3.buy_car(Auto1)


Autoconnect.show_available_cars()

