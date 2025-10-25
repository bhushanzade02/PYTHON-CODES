
def isPrime(num):
    if num < 2 :
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
    

    
x = int(input("Enter a number to check Prime "))
print(isPrime(x))