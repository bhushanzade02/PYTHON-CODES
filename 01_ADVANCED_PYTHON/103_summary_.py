new_list = [i ** 2 for i in range(1, 11)]
print(new_list)


new_list2 = [i for i in range(1, 11) if i % 2 == 0]
print(new_list2)

new_list3 = [i * 2 if (i % 2 == 0) else - i for i in range(1, 11)]
print(new_list3)
new_list4 = [[i for i in range(1, 4)] for j in range(3)]
print(new_list4)