n= int(input('enter a numbder'))


def prime_number(x):
    for i in range(2, int(x**0.5)+1):
        if x %  i ==0:
            return print('not a prime number')
    return print('prime number')

print(prime_number(n))