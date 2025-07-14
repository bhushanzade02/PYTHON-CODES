f = lambda n : 1 if n ==0 else n*f(n-1)
print(f(5)) 

#or 


def factorial(n):
    fact = 1
    if n < 0 :
        print("factorila of -ve no. not exist")
    if n ==0 :
        return 'factotrial of 0 is 1'
    else:
        for i in range(1,n +1):
            fact = fact * i
    print(f'factorial of {n} is {fact}')
    
print(factorial(5))