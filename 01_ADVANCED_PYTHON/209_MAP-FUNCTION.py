# using map function 

num = [1, 2, 3, 4]
def square(a):
    return a ** 2
    
square = list(map(square, num))
print(square)

# using lambda function 
sq= list(map(lambda a:a**2,num))
print(sq)


# using list copmrehension
sq2 = [i ** 2 for i in num]
print(sq2)