class Phone:
    def __init__(self, brand, model_name, price):
        self.brand=brand 
        self.model_name = model_name
        self.price = price


    def make_a_call(self, phone_number):
        print(f"calling{phone_number}.....")

    def full_name(self):
        return f"{self.brand} {self.model_name}"



p1 = Phone("Apple", "Iphone", 10000)
p2 = Phone("Redmi", "Note 9", 5000)

print(p1.make_a_call(9623613486))
print(p2.brand,p2.model_name,p2.price)
print(p2.__dict__)