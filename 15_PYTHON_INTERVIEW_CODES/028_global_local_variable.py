x = 5           # global variable
def f1():
    global x
    x = 15     # UPDATE GLOBAL VARIABLE 
    y = 10     # LOCAL VARIABLE
    print("x = %d y = %d"%(x,y))
    
f1()
print(x)
     