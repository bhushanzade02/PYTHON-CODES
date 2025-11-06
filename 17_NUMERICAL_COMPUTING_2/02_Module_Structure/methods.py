
import matplotlib.pyplot as plt
import numpy as np
class DiffEquation:

    def __init__(self, x0, y0, h, x_end):
        self.x0 = x0
        self.y0 = y0
        self.h = h
        self.x_end = x_end

    def euler(self, f):
        x = self.x0
        y = self.y0

        print("\n eulers method:")
        print(f"{'x':<10}{'y':<15}")
        print("-" * 40)

        while x < self.x_end:
            y = y + self.h * f(x, y)
            x = x + self.h
            print(f"{x:<10.4f}{y:<15.4f}")

        return y

    def mod_euler(self, f):
        x = self.x0
        y = self.y0

        print("\n mod eul method:")
        print(f"{'x':<10}{'y_pred':<15}{'y_corr':<15}")
        print("-" * 45)

        while x < self.x_end:
            y_pred = y + self.h * f(x, y)
            y_corr = y + (self.h / 2) * (f(x, y) + f(x + self.h, y_pred))
            x = x + self.h
            y = y_corr
            print(f"{x:<10.4f}{y_pred:<15.4f}{y_corr:<15.4f}")

        return y

    def rk4(self, f):
        x = self.x0
        y = self.y0

        print("\n runge-kutta method:")
        print(f"{'x':<10}{'y':<15}")
        print("-" * 40)

        while x < self.x_end:
            k1 = self.h * f(x, y)
            k2 = self.h * f(x + self.h / 2, y + k1 / 2)
            k3 = self.h * f(x + self.h / 2, y + k2 / 2)
            k4 = self.h * f(x + self.h, y + k3)
            k = (k1 + 2*k2 + 2*k3 + k4) / 6
            x += self.h
            y += k
            print(f"{x:<10.4f}{y:<15.4f}")

        return y
    
    
    
    def plot_error_vs_h(self, f, true_solution):
            import numpy as np
            hs = [0.5, 0.25, 0.1, 0.05, 0.01]
            euler_err, mod_euler_err, rk4_err = [], [], []

            for h in hs:
                self.h = h
                y_true = true_solution(self.x_end)
                y_euler = self.euler(f)
                y_mod_euler = self.mod_euler(f)
                y_rk4 = self.rk4(f)

                euler_err.append(abs(y_true - y_euler))
                mod_euler_err.append(abs(y_true - y_mod_euler))
                rk4_err.append(abs(y_true - y_rk4))

            plt.loglog(hs, euler_err, 'o-', label='Euler')
            plt.loglog(hs, mod_euler_err, 's-', label='Modified Euler')
            plt.loglog(hs, rk4_err, '^-', label='Runge-Kutta 4')
            plt.xlabel('Step size (h)')
            plt.ylabel('Absolute Error at x_end')
            plt.title('Error vs Step Size (h)')
            plt.legend()
            plt.grid(True, which="both", ls="--")
            plt.show()


class PowerMethod:
    """
    Power Method to find the dominant eigenvalue and eigenvector of a matrix.
    """

    def __init__(self, A, tolerance=1e-6, max_iterations=1000):
        self.A = np.array(A, dtype=float)
        self.tolerance = tolerance
        self.max_iterations = max_iterations

    def run(self, initial_vector=None):
        n = self.A.shape[0]

        # If no initial vector is given, start with ones
        if initial_vector is None:
            x = np.ones(n)
        else:
            x = np.array(initial_vector, dtype=float)

        # Normalize initial vector
        x = x / np.linalg.norm(x)
        lambda_old = 0

        for i in range(self.max_iterations):
            # Multiply A * x
            x_new = np.dot(self.A, x)

            # Normalize
            x_new = x_new / np.linalg.norm(x_new)

            # Rayleigh quotient for eigenvalue approximation
            lambda_new = np.dot(x_new.T, np.dot(self.A, x_new))

            # Check for convergence
            if abs(lambda_new - lambda_old) < self.tolerance:
                print(f"\n Converged in {i+1} iterations.")
                return lambda_new, x_new

            x = x_new
            lambda_old = lambda_new

        print("\n Did not converge within max iterations.")
        return lambda_new, x_new
