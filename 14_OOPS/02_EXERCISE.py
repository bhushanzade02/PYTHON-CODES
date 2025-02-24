class Laptop:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        


lp1 = Laptop('Dell', 'inp 14', 63000)
lp2 = Laptop('ACER', 'inp 15', 55000)

print(lp2.model)
print(lp1.brand)
print(lp1.price)

