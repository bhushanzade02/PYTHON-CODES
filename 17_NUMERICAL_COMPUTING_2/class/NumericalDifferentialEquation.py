 

import sympy as sp



class DiffEquation:

    def __init__(self, x0, y0, h, x_end):
        self.x0 = x0
        self.y0 = y0
        self.h = h
        self.x_end = x_end

    def euler(self, f):
        x = self.x0
        y = self.y0
        
        
        print("eulers method : " )
        print(f"{'x':<10}{'y':<15}")
        print("-"*25)

        while x < self.x_end:
            y = y + self.h * f(x, y)
            x = x + self.h
            print(f"{x:<10.4f}{y:<15.4f}")

        return y

    def mod_euler(self, f):
        x = self.x0
        y = self.y0
        
        print("modified eulers Method : ")
        print(f"{'x':<10}{'y_pred':<15}{'y_corr':<15}")
        print("-"*40)

        while x < self.x_end:
            y_p = y + self.h * f(x, y)
            y_c = y + (self.h/2) * (f(x, y) + f(x + self.h, y_p))  
            x = x + self.h
            y = y_c
            print(f"{x:<10.4f}{y_p:<15.4f}{y_c:<15.4f}")

        return y


if __name__ == "__main__":

    x0 = float(input("x0 = "))
    y0 = float(input("y0 = "))
    h = float(input("h = "))
    x_end = float(input("x target = "))
    
  
    x, y = sp.symbols('x y')
    f_str = input("Enter dy/dx = f(x, y) (use x and y): ")
    expr = sp.sympify(f_str)
    f = sp.lambdify((x, y), expr, "math") 

    de = DiffEquation(x0, y0, h, x_end)

    eul = de.euler(f)
    print(f"y({x}) = {eul:.4f}\n")

    mod_eul = de.mod_euler(f)
    print(f"y({x}) = {mod_eul:.4f}")