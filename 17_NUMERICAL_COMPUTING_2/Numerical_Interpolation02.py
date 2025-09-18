class Interpolation:
    def __init__(self, ax, ay):
        self.ax = ax
        self.ay = ay
        self.n = len(ax)
        self.h = ax[1] - ax[0] if self.n > 1 else 0

#------------------------------------------------------------

    # difff table
    def build_diff_table(self):
        n = self.n
        diff = [[0 for j in range(n)] for i in range(n)]
        for i in range(n):
            diff[i][0] = self.ay[i]

        for j in range(1, n):
            for i in range(n - j):
                diff[i][j] = diff[i + 1][j - 1] - diff[i][j - 1]
        return diff
    
#------------------------------------------------------------

    # newton forward
    def newton_forward(self, x, order=4):
        diff = self.build_diff_table()
        i = 0
        while i < self.n and self.ax[i] <= x:
            i += 1
        i -= 1

        p = (x - self.ax[i]) / self.h
        yp = self.ay[i]

        nr, dr = 1, 1
        for k in range(1, min(order, self.n)):
            nr *= p - k + 1
            dr *= k
            yp += (nr / dr) * diff[i][k]
        return yp
    
#------------------------------------------------------------

# newton backward 
    def newton_backward(self, x, order=4):
        diff = self.build_diff_table()
        i = self.n - 1
        p = (x - self.ax[i]) / self.h
        yp = self.ay[i]

        nr, dr = 1, 1
        for k in range(1, min(order, self.n)):
            nr *= p + k - 1
            dr *= k
            yp += (nr / dr) * diff[i - k][k]
        return yp
    
#------------------------------------------------------------
#------------------------------------------------------------

    # lagrange 
    def lagrange(self, x):
        y = 0
        for i in range(self.n):
            nr, dr = 1, 1
            for j in range(self.n):
                if i != j:
                    nr *= (x - self.ax[j])
                    dr *= (self.ax[i] - self.ax[j])
            y += (nr / dr) * self.ay[i]
        return y

#------------------------------------------------------------
#------------------------------------------------------------

#   Central Differences formula


    # gauss forward
    def gauss_forward(self, x):
        diff = self.build_diff_table()
        m = self.n // 2
        p = (x - self.ax[m]) / self.h
        yp = self.ay[m]

        nr, dr = 1, 1
        k = 1
        for j in range(1, self.n):
            if j % 2 != 0:
                nr *= (p - (k - 1) / 2)
            else:
                nr *= (p + (k // 2))
            dr *= j
            yp += (nr / dr) * diff[m - (j // 2)][j]
            k += 1
        return yp
    
#------------------------------------------------------------
    
    # gauss backward
    def gauss_backward(self, x):
        diff = self.build_diff_table()
        m = self.n // 2
        p = (x - self.ax[m]) / self.h
        yp = self.ay[m]

        nr, dr = 1, 1
        k = 1
        for j in range(1, self.n):
            if j % 2 != 0:
                nr *= (p + (k - 1) / 2)
            else:
                nr *= (p - (k // 2))
            dr *= j
            yp += (nr / dr) * diff[m - (j // 2)][j]
            k += 1
        return yp

#------------------------------------------------------------
    
    def stirling(self, x):
        diff = self.build_diff_table()
        m = self.n // 2   
        p = (x - self.ax[m]) / self.h
        yp = self.ay[m]   

        nr, dr = 1, 1
        k = 1
        for j in range(1, self.n):
            dr *= j
            if j % 2 != 0: 
                nr *= p
                yp += (nr / dr) * ((diff[m - (k - 1)][j] + diff[m - (k - 1)][j]) / 2)
                nr *= (p**2 - (k**2))
                k += 1
            else:         
                nr *= (p**2 - (k - 1)**2)
                yp += (nr / dr) * diff[m - (j // 2)][j]
        return yp


#------------------------------------------------------------
#------------------------------------------------------------


if __name__ == "__main__":
    
    n = int(input("Enter number of points: "))

    ax, ay = [], []
    print("Enter x y values:")
    for _ in range(n):
        values = input().split()
        ax.append(float(values[0]))
        ay.append(float(values[1]))

    x = float(input("Enter value of x to interpolate: "))

    interp = Interpolation(ax, ay)

#------------------------------------------------------------
 # interpolation at Start and Of
    print(f"N/w forward: {interp.newton_forward(x):.2f}")

    print(f"N backward: {interp.newton_backward(x):.2f}")

#------------------------------------------------------------
    print(f"lagrange: {interp.lagrange(x):.2f}")
#------------------------------------------------------------

 # Central Difference Formula 

    print(f"Gauss Forward: {interp.gauss_forward(x):.2f}")

    print(f"Gaus Backward: {interp.gauss_backward(x):.2f}")

    print(f"stirling: {interp.stirling(x):.2f}")

#------------------------------------------------------------