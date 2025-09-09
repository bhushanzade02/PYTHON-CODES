# sq = ( x**2 for x in range(1,6))
# print(sq)
# for i in sq:
#     print(i)


# def fib(n):
#     series =[]
#     a = 0 
#     b = 1
#     for i in range(2,n):
#         c = a + b
#         series.append(c)
#         a = b 
#         b = c
#     return series


def fibo():
    a , b = 0 ,1 
    while True:
        yield a 
        a ,b = b ,a + b

fib = fibo()
for _ in range(10):
    print(next(fib))
