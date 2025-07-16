class A:
    def __init__(self,a):
        self.a = a 
    
    def __add__(self,o):
        return self.a + o.a
    


obj1 = A(1)
obj2 = A(2)
obj3 = A("Geeks")
obj4 = A("for")


print(obj1 + obj2 )
print(obj3 + obj4 )


print(A.__add__(obj1,obj2))
print(A.__add__(obj3,obj4))

print(obj1.__add__(obj2))
print(obj3.__add__(obj4))