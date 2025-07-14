class Animal:
    
    def __init__(self,name):
        self.name = name
        
    def sound(self):
        raise NotImplementedError(" sublass must implment this method")
    
    
class Dog(Animal):
    def sound(self):
        
        
        return "WWOOOFFF!"
    
a= Animal("Generic ANimal")
d = Dog("Buddy")


print(a.name)
print(d.name)

print(d.sound())