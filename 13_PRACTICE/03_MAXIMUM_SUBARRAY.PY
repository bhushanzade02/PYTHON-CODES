

n = [1, 2, 3, 4, 5]

for st in range(len(n)):
    for end in range(st, len(n)):
        for i in range(st, end + 1):
            print(n[i], end=' ')
        print()  
