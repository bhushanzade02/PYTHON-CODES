fruits = ['grapes', 'mango', 'apple']
fruits.sort()
print(fruits)


fruits2 = ('grapes', 'mango', 'apple')
print(sorted(fruits2))
print(fruits2) 



fruits3 = {'grapes', 'mango', 'apple'}
print(sorted(fruits3))
b = sorted(fruits3)
print(b)
print(f" dictionary {fruits3}")


guitars = [
    {'modek1': 'yaamaha f310 ', 'price': 8000},
    {'modek1': 'faith naptune ', 'price': 3000},
    {'modek1': 'faith apoolo venus', 'price': 4000},
    {'modek1': ' taylor 814 ce', 'price': 5000},
]

print(max(guitars , key = lambda d:d['price']))
print(sorted(guitars , key = lambda d:d['price']))
print(sorted(guitars , key = lambda d:d['price'],reverse=True))


