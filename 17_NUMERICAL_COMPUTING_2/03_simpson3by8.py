def y(x):
    return 1 / (1 + x**2)

def simpson38():

    n = int(input("Enter the on. of subintrval (multiple of 3): "))
    
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