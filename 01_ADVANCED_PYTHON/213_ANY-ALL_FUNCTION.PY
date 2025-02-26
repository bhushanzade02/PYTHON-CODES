num = [2, 4, 6,7,3, 8, 10]

num3=[]
for i in num:
    if i % 2 == 0:
        num3.append(i)
print(num3)



num4 = [i for i in num if i % 2 == 0]
print(num4)


num5 = [i % 2 == 0 for i in num]
print(any(num5))