class Vehicle:
    def __init__(self, brand, model, price):
        # Encapsulacion
        self.brand = brand
        self.model = model
        self.price = price
        self.is_available = True

    def sell (self):
        if self.is_available:
            self.is_available = False
            print(f'El vehiculo: {self.brand} a sido vendido')
        else:
            print(f'El vehiculo: {self.brand} no se encuentra disponible')

    # Abstracion

    def check_available (self):
        return self.is_available
    
    def get_price(self):
        return self.price

    def start_engine(self):
        raise NotImplementedError('Este metodo debe ser implementado por la subclase')
        
    def stop_engine(self):
        raise NotImplementedError('Este metodo debe ser implementado por la subclase')

# Herencia

class Car(Vehicle):
        
        # Polimorfismo
        
        def start_engine(self):
            if not self.is_available:
                return f'El motor de {self.brand} esta en marcha'
            else:
                return f'El auto {self.brand} no está disponible'
            
        def stop_engine(self):
            if self.is_available:
                return f'El motor de {self.brand} está apagado'
            else:
                return f'El auto {self.brand} no está disponible'
            
class Bike(Vehicle):
        def start_engine(self):
            if not self.is_available:
                return f'El motor de {self.brand} esta en marcha'
            else:
                return f'El auto {self.brand} no está disponible'
            
        def stop_engine(self):
            if self.is_available:
                return f'La bicicleta {self.brand} está rodando'
            else:
                return f'La bicicleta {self.brand} no está disponible'
            
class Truck(Vehicle):
        def start_engine(self):
            if not self.is_available:
                return f'El motor de {self.brand} esta en marcha'
            else:
                return f'El auto {self.brand} no está disponible'
            
        def stop_engine(self):
            if self.is_available:
                return f'El motor de {self.brand} está apagado'
            else:
                return f'El auto {self.brand} no está disponible'
            
class Customer:
    def __init__(self, name):
        self.name = name
        self.purchased_vehicles = []
    
    def buy(self, vehicle: Vehicle):
        if vehicle.check_available():
            vehicle.sell()
            self.purchased_vehicles.append(vehicle)
        else:
            print(f'El vehiculo {vehicle.brand} no esta disponible')

    def inquire_vehicle(self, vehicle: Vehicle):
        if vehicle.check_available():
            availability = 'disponible'
        else:
            availability = 'no disponible'
        print(f'El vehiculo {vehicle.brand} esta {availability}, y su precio es {vehicle.get_price()}')

class Dealiship:
    def __init__(self):
        self.inventory = []
        self.customers = []

    def add_vehicle (self, vehicle: Vehicle):
        self.inventory.append(vehicle)
        print(f'El vehiculo {vehicle.brand} ha sido agregado al inventario de forma correcta')
    
    def register_customer(self, customer: Customer):
        self.customers.append(customer)
        print(f'El Cliente {customer.name} ha sido agregado al registro de forma correcta')

    def show_available_vehiculo(self):
        for vehicle in self.inventory:
            if vehicle.check_available():
                print(f'- {vehicle.brand} por {vehicle.get_price()}')


# Creamoos vehiculos
car = Car('Toyota', 'Etios', '15000')
bike = Bike('Polygon', 'Siskiu', '3000')
trunck = Truck('Scania', 'Poto', '40000')

# Creamos clientes
customer1 = Customer('Rogelio')
customer2 = Customer('Alfonso')
customer3 = Customer('Ruperto')

# Creamos la tienda
dealership = Dealiship()

# Agragamos vehiculos al inventario
dealership.add_vehicle(car)
dealership.add_vehicle(bike)
dealership.add_vehicle(trunck)

# Registramos clientes en la tienda
dealership.register_customer(customer1)
dealership.register_customer(customer2)
dealership.register_customer(customer3)

# Mostramos inventario
dealership.show_available_vehiculo()

car.start_engine()

customer1.inquire_vehicle(car)

customer1.buy(car)

dealership.show_available_vehiculo()