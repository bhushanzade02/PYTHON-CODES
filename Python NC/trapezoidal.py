# fuction one 
def z(x):
    return ((x**3) +1)**0.5
a = 1 
b= 4
n =6

# #function 2 
# def y(x):
#     return x * (2.71828 **(2*x))
# a = 0
# b = 3
# n = 4

def trapezoidal(y):
    h = (b-a ) / n
    s =  y(a) + y(b)
    for i in range(n):
        s+=2*y(a + i * h)
    result = (h/2) * s
    print(f"the value of integral {result}")
    
    
trapezoidal(z)


