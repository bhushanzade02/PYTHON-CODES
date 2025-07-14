def isPrime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
    
    
def Prime_Generator(n):
    num = 2 
    while(n):
        if isPrime(num):
            yield num
            n-=1
        num+=1
    
    
    
    
x = int(input("ENter a NUmber of prime Required "))
it = Prime_Generator(x)


for e in it :
    print(e,end = " ")
