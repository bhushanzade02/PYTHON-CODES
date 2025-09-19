
"""Newton forward interpolation"""

def Newton_Forward():
    n = int(input("Enter the value of n"))
    ax=[] 
    ay=[]

    for i in range(n+1):
        print(i)
        values = input().split()
        a = float(values[0])
        b = float(values[1])
        ax.append(a)
        ay.append(b)

    h = ax[1] - ax[0]

    x = float(input("enter the value of x for which y value is wanted "))

    s = len(ay)
    order = 4
    diff = [[0 for j in range(order+1)] for i in range(s)]
    for i in range(n):
        diff[i][1] = ay[i +1] - ay[i]

    for j in range(2,order+1):
        for i in range((n-j + 1 )):
            diff[i][j]= diff[i+1][j-1] - diff[i][j-1]


    i = 0
    while i < n and ax[i] <= x:
        i += 1
    i -= 1

    p = ( x - ax[i]) /h
    yp = ay[i]


    nr , dr = 1 , 1

    for k in range(1,order + 1):
        nr *= p - k + 1
        yp += (nr / dr) * diff[i][k]

    print(f"when x = {x}  and y = {yp:.2f}")




"""Newton backward interpolation"""

def Newton_Backward():
    n = int(input("Enter the value of n"))
    ax=[] 
    ay=[]

    for i in range(n+1):
        print(i)
        values = input().split()
        a = float(values[0])
        b = float(values[1])
        ax.append(a)
        ay.append(b)

    h = ax[1] - ax[0]

    x = float(input("enter the value of x for which y value is wanted "))

    s = len(ay)
    order = min(4,n)
    diff = [[0 for j in range(order+1)] for i in range(s)]
    for i in range(n):
        diff[i][1] = ay[i +1] - ay[i]

    for j in range(2,order+1):
        for i in range((n-j + 1 )):
            diff[i][j]= diff[i+1][j-1] - diff[i][j-1]

    i = n
    p = ( x - ax[i]) /h
    yp = ay[i]


    nr , dr = 1 , 1
    for k in range(1,order + 1):
        nr *= ( p + k - 1)
        dr *= k
        yp += (nr / dr) * diff[i-k][k]

    print(f"when x = {x}  and y = {yp:.2f}")



"""LAGRANGE INTERPOLATION"""

def lagrange_Interpolation():
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



"""Gauss Forward Interpolation"""

def Gauss_Forward():
    n = int(input("Enter the value of n: "))
    ax = []
    ay = []

    for i in range(n):
        values = input("Enter x y: ").split()
        a = float(values[0])
        b = float(values[1])
        ax.append(a)
        ay.append(b)

    h = ax[1] - ax[0]

    x = float(input("Enter the value of x for which y is wanted: "))

 
    diff = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        diff[i][0] = ay[i]

    for j in range(1, n):
        for i in range(n - j):
            diff[i][j] = diff[i+1][j-1] - diff[i][j-1]

    # Start with middle point
    m = n // 2
    p = (x - ax[m]) / h
    yp = ay[m]

    # Apply Gauss forward formula
    nr, dr = 1, 1
    k = 1
    for j in range(1, n):
        if j % 2 != 0:
            nr *= p - (k - 1) / 2
        else:
            nr *= p + (k // 2)
        dr *= j
        yp += (nr / dr) * diff[m - (j // 2)][j]
        k += 1

    print(f"When x = {x}, y = {yp:.2f}")


"""Gauss Backward Interpolation"""

def Gauss_Backward():
    n = int(input("Enter the value of n: "))
    ax = []
    ay = []

    for i in range(n):
        values = input("Enter x y: ").split()
        a = float(values[0])
        b = float(values[1])
        ax.append(a)
        ay.append(b)

    h = ax[1] - ax[0]

    x = float(input("Enter the value of x for which y is wanted: "))

    # Build difference table
    diff = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        diff[i][0] = ay[i]

    for j in range(1, n):
        for i in range(n - j):
            diff[i][j] = diff[i+1][j-1] - diff[i][j-1]

    # Start with middle point
    m = n // 2
    p = (x - ax[m]) / h
    yp = ay[m]

    # Apply Gauss backward formula
    nr, dr = 1, 1
    k = 1
    for j in range(1, n):
        if j % 2 != 0:
            nr *= p + (k - 1) / 2
        else:
            nr *= p - (k // 2)
        dr *= j
        yp += (nr / dr) * diff[m - (j // 2)][j]
        k += 1

    print(f"When x = {x}, y = {yp:.2f}")
