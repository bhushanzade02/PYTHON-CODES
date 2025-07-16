class Shape:
    def area(self):
        raise NotImplementedError("subclas Must implement")
    
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width
        
    def area(self):
        print(f"the area of rectangle : {self.length * self.width}")
        
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side , side)
    
    
    def area(self):
        print(f'the area of sq id {self.length **2}')
        
        
Rect = Rectangle(2,3)
my_sq = Square(4)

Rect.area()
my_sq.area()
    