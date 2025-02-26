def fun(int1, int2):
    add = int1 + int2
    mul = int1 * int2
    return add, mul

print(fun(2, 3))


add, mul = fun(2, 3)

print(add)
print(mul)