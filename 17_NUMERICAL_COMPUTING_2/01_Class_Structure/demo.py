import sympy as sp
import math
import matplotlib.pyplot as plt

class DiffEquation:
    def __init__(self, x0, y0, h, x_end):
        self.x0 = x0
        self.y0 = y0
        self.h = h
        self.x_end = x_end

    def euler(self, f):
        x = self.x0
        y = self.y0

        # print("Euler's Method:")
        while x < self.x_end:
            y = y + self.h * f(x, y)
            x = x + self.h
        return y

    def mod_euler(self, f):
        x = self.x0
        y = self.y0

        # print("Modified Euler's Method:")
        while x < self.x_end:
            y_p = y + self.h * f(x, y)
            y_c = y + (self.h / 2) * (f(x, y) + f(x + self.h, y_p))
            x = x + self.h
            y = y_c
        return y

    def rk4(self, f):
        x = self.x0
        y = self.y0

        # print("Runge-Kutta 4 Method:")
        while x < self.x_end:
            k1 = self.h * f(x, y)
            k2 = self.h * f(x + self.h / 2, y + k1 / 2)
            k3 = self.h * f(x + self.h / 2, y + k2 / 2)
            k4 = self.h * f(x + self.h, y + k3)
            k = (k1 + 2*k2 + 2*k3 + k4) / 6
            x += self.h
            y += k
        return y


if __name__ == "__main__":
    # Given ODE and exact solution
    f = lambda x, y: -2*y + math.exp(-x)
    exact = lambda x: math.exp(-2*x) + (1/3)*math.exp(-x)

    x0, y0, x_end = 0, 1, 2
    h_values = [0.5, 0.25, 0.1, 0.05, 0.025, 0.01]

    euler_errors = []
    mod_euler_errors = []
    rk4_errors = []

    for h in h_values:
        de = DiffEquation(x0, y0, h, x_end)
        y_euler = de.euler(f)
        y_mod_euler = de.mod_euler(f)
        y_rk4 = de.rk4(f)

        y_exact = exact(x_end)
        euler_errors.append(abs(y_euler - y_exact))
        mod_euler_errors.append(abs(y_mod_euler - y_exact))
        rk4_errors.append(abs(y_rk4 - y_exact))

    # Plotting error vs step size
    plt.figure(figsize=(8, 6))
    plt.loglog(h_values, euler_errors, 'o-', label='Euler')
    plt.loglog(h_values, mod_euler_errors, 's-', label='Modified Euler')
    plt.loglog(h_values, rk4_errors, '^-', label='Runge-Kutta 4')

    plt.xlabel('Step size (h)')
    plt.ylabel('Absolute Error at x=2')
    plt.title('Error Behavior as Step Size Decreases')
    plt.legend()
    plt.grid(True, which="both", ls="--")
    plt.show()
