# MAP
def square(a):
    return a ** 2
    
li = [1, 2, 3, 4]
# print(list(map(square, li)))


# now defining our own function 


def my_map(func, l):
    new_list = []
    for item in l:
        new_list.append(func(item))
    return new_list
 
print(my_map(square, li))
print(my_map(lambda a: a ** 2, li))
print(my_map(lambda a: a ** 3, li))



# uisng list comprehension 
def my_map2(func, l):
    return [func(item) for item in l]
    
print (my_map2(lambda a: a**3, li))