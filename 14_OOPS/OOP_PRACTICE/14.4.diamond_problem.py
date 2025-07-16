class Class1:
    def m(self):
        print("in class")
class Class2(Class1):
    def m(self):
        print("in class 2")
class Class3(Class1):
    def m(self):
        print("in class 3")
        
class Class4(Class2, Class3):
    pass


obj = Class4()
obj.m()