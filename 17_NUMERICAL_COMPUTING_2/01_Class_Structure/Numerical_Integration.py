# import sympy as sp
# import numpy as np


class Numerical_Integration:
    def __init__(self, func, a, b, n):
        self.func = func
        self.a = a
        self.b = b
        self.n = n
        
    def trapezoidal(self):
        n = self.n
        x0 , xn =self.a , self.b
        h = (xn - x0) / n
        all_terms = 0 
        for i in range(1, n):
            xi = x0 + i * h
            all_terms += y(xi)
        integral_value = (h/2) * (y(x0) + 2 * (all_terms) + y(xn))
        return  f"the aprroximate value of integral is : {integral_value:.5f} by trapezoidal rule"
    
    
    def simpson13(self):
        a, b , n = self.a ,self.b , self.n
        if n % 2 != 0 :
            print("Errrorrr")
        else :
            x0 = a
            xn = b 
            h = (xn - x0) / n
            
            odd_terms = 0
            for i in range(1,n,2):
                xi = x0 + i * h 
                odd_terms += 4 * y(xi)
                
            even_terms = 0 
            for i in range(2, n, 2):
                xi = x0 + i * h
                even_terms += 2 * y(xi)
            
            integral_value = (h/3) *(y(x0) + odd_terms + even_terms + y(xn) )
            return f"the approximate value of integral is : {integral_value:.5f} by simpson 1/3 rule"
    
    
    def simpson38(self):
        a , b, n = self.a , self.b , self.n 
        if n % 3 != 0 :
            print("Errrorrr")
        else :
            x0 , xn = a , b
            h = (xn - x0 ) / n
            
            non_mod_sum = 0 
            for i in range(1,n):
                if i % 3 != 0 :
                    xi = x0 + i * h
                    non_mod_sum += y(xi)
            
            mod3_sum = 0 
            for i in range(3,n,3):
                xi = x0 + i * h 
                mod3_sum += y(xi)
            
            integral_value = ((3 * h)/8) * ( y(x0) + 3 * (non_mod_sum) + 2 * (mod3_sum) + y(xn) )
            return f"the aprroximate value of integral is : {integral_value:.5f} by simpson 3/8 rule"

                             
    
if __name__== "__main__":
    
    # x = sp.symbols('x')
    # exp_str = input("enter the function : ")
    # expr = sp.sympify(exp_str)
    # y = sp.lambdify(x, expr, "math")    
    
    y = lambda x : 1/(1 + x**2)
     
    a = int(input("Enter Lower Limit a : "))
    b = int(input("Enter upper Limit b : "))
    n = int(input("Enter the number of Sub-Intervals n : "))
    
    num = Numerical_Integration(y, a ,b , n )
 
    # print(expr)
    print()
    print(num.trapezoidal())
    
    print(num.simpson13())
    
    print(num.simpson38())

    print(num.Euler())