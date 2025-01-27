def greater(a, b):
    if a > b:
        return a
    return b


def new_greatest(a, b, c):
    bigger = greater(a, b)
    return greater(bigger, c)
    

print(new_greatest(10,29,2))