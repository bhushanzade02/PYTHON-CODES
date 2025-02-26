# squares = []
# for i in range(1, 11):
#     squares.append(i ** 2)
#     print(i)
#     print(squares)
    
# square2 = [i ** 2 for i in range(1, 11)]
# print(square2)


# negno = [-i for i in range(1,11)]
# print(negno)





name = ['bhushan', 'sarthak', 'rahul']

# new_list = []
# for name in name:
#     new_list.append(name[0])
# print(new_list)
new_list = [name[0] for name in name]
print(new_list)