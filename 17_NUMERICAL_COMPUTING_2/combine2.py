
"""LAGRANGE INTERPOLATION"""

def lagrange():
    Ax = []
    Ay = []

    n = int(input("enter the value of n"))

    for i in range(n):
        values = input().split()
        a = float(values[0])
        b = float(values[1])
        Ax.append(a)  
        Ay.append(b)  

    x = int(input("enter the value for you want to calculate"))

    for i in range(n):
        print(Ax)

    for i in range(n):
        print("Ay",Ay)
    
    y= 1
    for i in range(n):
        nr = dr = 1
        for j in range(n):
            if i != j :
                nr *= x - Ax[j]
                dr *= Ax[i] - Ax[j]
        y += (nr/dr) * Ay[i]

    print(f"when x = {x} then y =  {y}")



print(lagrange())



"""_SIMPSON 1 / 3 RULE_"""

def y(x):
        return 1 / (1 + x**2)


def simpson13():

    n = int(input("Enter the no. of subintervals (must be even): "))
    if n % 2 != 0:
        print("Error")
    else:   
        x0 = float(input("Enter the value of a: "))
        xn = float(input("Enter the value of b: "))

        h = (xn - x0) / n
        
        odd_terms = 0
        for i in range(1, n, 2):
            xi = x0 + i * h
            odd_terms += 4 * y(xi)

        even_terms = 0
        for i in range(2, n, 2):
            xi = x0 + i * h
            even_terms += 2 * y(xi)

        integral_value = (h / 3) * (y(x0) + odd_terms + even_terms + y(xn))

        return (f"The approximate integral value is: {integral_value}")


print(simpson13())




"""_SIMPSON 3 / 8 RULE_"""

def y(x):
    return 1 / (1 + x**2)

def simpson38():

    n = int(input("Enter the on.of subinterval multiple of 3 : "))
    
    if n % 3 != 0:
        print("Error ")
    else :
        x0 = float(input("Enter the value of a: "))
        xn = float(input("Enter the value of b: "))

        h = (xn - x0) / n
    
        non_mod3_sum = 0
        for i in range(1, n):
            if i % 3 != 0:
                xi = x0 + i * h
                non_mod3_sum += y(xi)
        
        mod3_sum = 0
        for i in range(3, n, 3):
            xi = x0 + i * h
            mod3_sum += y(xi)

        integral_value = (3 * h / 8) * (y(x0) + 3 * non_mod3_sum + 2 * mod3_sum + y(xn))
        
        return integral_value

    
print(simpson38())




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
