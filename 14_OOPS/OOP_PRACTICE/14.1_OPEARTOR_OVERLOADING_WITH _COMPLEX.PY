class Complex:
    def __init__(self,a,b):
        self.a = a
        self.b = b
        
    def __add__(self, other):
        return self.a + other.a ,self.b + other.b

ob1= Complex(1,2)
ob2= Complex(3,5)


ob3 = ob1 + ob2
print(ob3)