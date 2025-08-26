def fibonacci(n):
    a = 0 
    b = 1
    series = []

    for i in range(2,n):
        c = a + b
        series.append(c)
        a = b
        b = c
    return series


print(fibonacci(10))























