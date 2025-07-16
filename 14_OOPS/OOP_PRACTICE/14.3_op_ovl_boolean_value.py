class Myclass:
    def __init__(self,value):
        self.value = value
    
    def __and__(self, other):
        return Myclass(self.value and other.value)
    
    
a=Myclass(True)
b= Myclass(False)

c = a&b
print(c)


c.value is False