
# eulers method 



def function(x1 , y1):
    return x1 + y1


x0 = float(input("enter the value of x : "))
y0 = float(input("enter the value of y : "))
h  = float(input("enter the step size of h : "))

x = float(input("enter value of x to compute y : "))

x1 = x0 
y1 = y0 


while True:
    if (x1 > x) :
        break
    y1 += h* function(x1, y1)
    x1 += h
    print(f" when x = {x1} y = {y1}")

    