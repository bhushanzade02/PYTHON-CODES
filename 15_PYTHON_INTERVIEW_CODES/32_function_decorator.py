# function decortaor 
def welcome(fx):
    def mfx(*t,**d):
        print("Before hello function")
        fx(*t , **d)
        print("thanks for using this Function")
    return mfx

#decorator function without argument 
@welcome
def hello():
    print("hello !")


#decorator function with argumentS
@welcome
def add(a,b):
    print(a+b)
    
    
    
hello()
add(1,3)
    