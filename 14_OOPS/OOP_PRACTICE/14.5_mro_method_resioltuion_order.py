class Class1:
    def m(self):
        print("in class 1")
        
        
class Class2(Class1):
    def m(self):
        print("in class 2")
        super().m()
        
        
        
class Class3(Class1):
    def m(self):
        print("in class 3")
        super().m()
        
        
        
class Class4(Class2, Class3):
    def m(self):
        print("in class 4")
        super().m()
        
print(Class4.mro())
print(Class4.__mro__)