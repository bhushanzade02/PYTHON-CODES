
numbers=[3,4,2,1,5,6,9,8,10]
evens = set(filter(lambda a: a % 2 == 0, numbers))
# print(evens)

# for i in evens:
#     print(i)




new_even = [i for i in numbers if i % 2 == 0]

print(list(evens))
print(new_even)