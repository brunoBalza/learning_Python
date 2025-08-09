class Pizza:
    base_price = 5000

    def __init__(self, ingredientes: list[str]):
        self.ingredientes = ingredientes

    @classmethod
    def napolitana(cls):
        return cls(['Muzzarella', 'Tomate', 'Ajo'])

    @classmethod
    def actualizar_precio_base(cls, new_price):
        cls.base_price = new_price

    def precio_total(self):
        return self.base_price + len(self.ingredientes) * 100 

pizza = Pizza.napolitana()
print(pizza.ingredientes)


print(pizza.precio_total())

pizza.actualizar_precio_base(6000)
print(pizza.base_price)

