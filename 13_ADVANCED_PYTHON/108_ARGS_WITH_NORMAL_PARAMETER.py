# def multiply_nums(*args):
#     mul = 1;
#     for i in args:
#         mul *= i
#     return mul
# print(multiply_nums(1,2,3))



def mul_num(num1, *args):
    print(num1)
    print(args)
    mul=1
    for i in args:
        mul *= i
    return mul

print(mul_num(2,3,2))