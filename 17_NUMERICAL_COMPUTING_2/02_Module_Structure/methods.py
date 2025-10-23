
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
