lst1 = [1,2,3]
lst2 = [4,5,6]

result = []
for i in range(0,len(lst1)):
    print('i value',i)
    print('lst1 i ' , lst1[i])
    print('lst2 i ' , lst2[i])
    result.append(lst1[i]+lst2[i])
    print(result)

print(result)
