#fib


# def fib(n):
#     if n==1 or n== 0 :
#         return 1
#     else :
#         return fib(n-1) + (fib(n-2))
    
# print(fib(48))




def fibi(n):
    if n==1 or n ==2 :
        return 1 
    a ,b = 1,1
    for _ in range(2,n+1):
         a , b  = b , a+b
    return b


print(fibi(48))