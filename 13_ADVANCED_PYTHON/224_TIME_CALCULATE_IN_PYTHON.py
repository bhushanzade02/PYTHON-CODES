import time
t1 = time.time()
print("THIS IS LINE ONE ")
X = 5
if X == 5:
    for i in range(1, 10000):
        print("this is line one ")
print("this is line 2")
t2 = time.time()
print(t2-t1)