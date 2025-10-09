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
        print("-"*40)

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
    

    def rk4(self,f):
        x = self.x0
        y = self.y0

        print(" Runge kutta method : ")
        print(f"{'x':<20}{'y':<15}")
        print("-"*40)

        while True:
            if x == xend :
                break 
            k1 = h * f(x,y)
            k2 = h * f(x+h/2 , y+k1/2)
            k3 = h * f(x+h/2 , y+k2/2)
            k4 = h * f(x+h, y+k3)
            k = (k1 + (k2 + k3) * 2 + k4) / 6
            x += h
            y += k

            print(f"when x = {x:.4f}  y = {y:.4f} ")

        return y
    


if __name__ == "__main__":

    x0 = float(input("x0 = "))
    y0 = float(input("y0 = "))
    h = float(input("h = "))
    xend = float(input("x target = "))
    
  
    x, y = sp.symbols('x y')
    f_str = input("Enter dy/dx = f(x, y)   : ")
    expr = sp.sympify(f_str)
    f = sp.lambdify((x, y), expr, "math") 

    de = DiffEquation(x0, y0, h, xend)

    print("\n")

    eul = de.euler(f) 
    print(f"y({x}) = {eul:.4f}\n\n")

    mod_eul = de.mod_euler(f)
    print(f"y({x}) = {mod_eul:.4f}\n\n")

    rk4 = de.rk4(f)
    print(f"y({x}) = {rk4:.4f}")x` `