class Phone:
    def __init__(self, brand, model_name, price):
        self.brand=brand 
        self.model_name = model_name
        self.price = price
    
    @property
    def complete_specification(self):
        return f"{self.brand} {self.model_name} and price is {self.price}"

    def make_a_call(self, phone_number):
        print(f"calling{phone_number}.....")

    def full_name(self):
        return f"{self.brand} {self.model_name}"

phone1 = Phone('Redmi', 'note 9',1000)
print(phone1.complete_specification) #<_______we dont use bracket() after function called we declare this as @poperty


