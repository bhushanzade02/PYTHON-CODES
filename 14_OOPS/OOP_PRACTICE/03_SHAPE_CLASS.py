class shape:
    def __init__(self,color):
        self.color = color
        
    def area(self):
        raise NotImplementedError("sublclass must impllemented this method")
    
    
class circle(shape):
    
    
    def __init__(self , color ,radius):
        

        super().__init__(color)
        
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius **2
    
    
s= shape('red')
c= circle('blue', 5)


print(s.color)
print(c.color)
print(c.radius)
print(c.area())
