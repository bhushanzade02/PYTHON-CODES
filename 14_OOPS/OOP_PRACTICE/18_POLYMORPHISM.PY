class Shape:
    def area(self):
        return "Undefined"


class Rectangle(Shape):
    def __init__(self,lenght,width):
        self.lenght = lenght
        self.width = width
    
    
    def area(self):
        return self.lenght * self.width
    
    
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
        
    def area(self):
        return 3.14 * self.radius **2
    
    
    
shapes = [Rectangle(2,4),Circle(4)]


for shape in shapes:
    print(f"AREA is :{shape.area()}")