def average(*t):
    avg = sum(t)/len(t)
    return round(avg,2)

result1 = average(10,20,30,40,50,2,4,2,13,31,12)
result2 = average(23,32,34,12,45,44,7,88,7) 

print(result1)
print(result2)