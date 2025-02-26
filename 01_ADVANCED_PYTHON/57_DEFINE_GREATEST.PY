def great_three(a, b, c):
    if a > b and a >c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c
a=int(input("enter a number "))
b=int(input("enter a number "))
c = int(input("enter a number "))


biggest = great_three(a, b, c)


print(f'{biggest} is greatest Number ')