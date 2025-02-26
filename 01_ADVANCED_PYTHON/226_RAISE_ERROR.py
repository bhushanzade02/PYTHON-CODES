def add(a, b):
    if (type(a) is int) and (type(b) is int):
        return a + b
    raise TypeError("oops you are passing wrong data type to function")


b = add('2',3)
print(b)