class Phone:
    def __init__(self, brand, model_name, price):
        self.brand = brand
        self.model_name = model_name
        self.price = max(price, 0)
        
    def full_name(self):
        return f"{self.brand} {self.model_name}"
    
    def make_a_call(self, number):
        return f'calling {number}....'



class Smartphone(Phone):
    def __init__(self, brand, model_name, price, ram, internal_memory, rear_camera):
        Phone.__init__(self, brand, model_name, price)
        self.ram = ram
        self.internal_memory = internal_memory
        self.rear_camera = rear_camera

phone1 = Phone("Redmi", "Note 9", 7200)
smartphone =Smartphone('SAmsung','galaxy',60000,'8 Gb','60 MP')


print(smartphone.__dict__)