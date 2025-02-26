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
        super().__init__( brand, model_name, price)
        self.ram = ram
        self.internal_memory = internal_memory
        self.rear_camera = rear_camera

class FlagshipPhone(Smartphone):
     def __init__(self, brand, model_name, price, ram, internal_memory, rear_camera, front_camera):
        super().__init__( brand, model_name, price, ram, internal_memory, rear_camera)
        self.front_camera=front_camera
        




FP = FlagshipPhone('SAmsung', 'galaxy', 60000, '8 Gb','ssd', '60 MP', '12MP')
print(FP.full_name())

