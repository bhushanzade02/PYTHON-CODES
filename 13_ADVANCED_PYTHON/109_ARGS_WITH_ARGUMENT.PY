def mul_nums(*args):
    mul = 1
    print(args)
    for i in args:
        mul *= i
    return mul


n = list(range(1, 4))



print(mul_nums(*n))