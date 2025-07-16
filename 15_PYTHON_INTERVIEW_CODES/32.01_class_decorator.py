class Calculator:
    def __init__(self,func):
        self.function = func
    
    def __call__(self,*t,**d):
        result = self.function(*t,**d)
        return result**2 
    
    
@Calculator
def add(a,b):
    return a + b

print(add(10,20))
