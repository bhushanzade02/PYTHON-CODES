class Laptop:
    discount_percent=10
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
    def apply_discount(self):
        offer_price=(self.discount_percent/100)*self.price
        return self.price-offer_price
        


# Laptop.discount_percent=10
lp1 = Laptop('Dell', 'inp 14', 63000)
lp2 = Laptop('ACER', 'inp 15', 55000)


# offer = lp2.apply_discount()
# print("your offer",offer)
print(lp1.__dict__)
print(lp1.apply_discount())