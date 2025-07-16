class Geek:
    def __init__(self,name,age):
        self.geekname = name
        self.geekage = age
    
    
    def display(self):
        
        print("NAME: ", self.geekage)
        
        
        
obj = Geek("Bhushan",21)
print(dir(obj) )

print('NAME: ', obj.geekname)

obj.display()