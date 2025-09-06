
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