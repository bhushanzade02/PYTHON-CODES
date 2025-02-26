class Mobile:
    def __init__(self, name):
        self.name = name
    
class Mobilestore:
    def __init__(self):
        self.mobiles = []
        
    def add_mobile(self, new_mobile):
        if isinstance(new_mobile, mobile):
            self.mobiles.append(new_mobile)
        else:
            raise TypeError('new mobile should be object of mobile class')



oneplus = Mobile("one plu s6")
samsung = 'samsung galaxy s8'
mobostore = Mobilestore()
print(mobostore.mobiles)
