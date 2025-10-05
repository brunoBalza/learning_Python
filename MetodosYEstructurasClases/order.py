class Order:
    
    @staticmethod
    def calculate_tax(amount, tax_rate):
        return amount * (tax_rate / 100)
    
print(Order.calculate_tax(1000, 15))

class Order2:
    global_discount = 10

    def __init__(self, amount):
        self.amount = amount

    @classmethod        
    def update_global_discount(cls, new_discount):
        cls.global_discount = new_discount

Order2.update_global_discount(15)       
print(Order2.global_discount)
