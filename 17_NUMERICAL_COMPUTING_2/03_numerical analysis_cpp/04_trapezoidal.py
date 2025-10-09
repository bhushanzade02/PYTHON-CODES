

"""_TRAPEZOIDAL RULE_"""

def y(x):
    return 1 / (1+x**2)

def trapezoidal():
    n = int(input("Enter the no of subinterval "))
    x0 = int(input("Enter the value of a :"))
    xn = int(input("Enter the value of b :"))

    h = (xn - x0) / n

    
    all_terms = 0
    for i in range(1, n):
        xi = x0 + i * h
        all_terms += y(xi) 

    integral_value = ( h/2 ) * (y(x0) + 2 *(all_terms) + y(xn) ) 
    return integral_value

print(trapezoidal())
