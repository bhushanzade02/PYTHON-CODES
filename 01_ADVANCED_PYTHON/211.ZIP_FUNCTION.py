# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# zipped = zip(list1, list2)
# print(list(zipped))


# list2 = [1, 2]
# list3 = ['a', 'b', 'c']
# print(list(zip(list2, list3)))



# names= ['bhushan', 'siddhi']
# scores = [90, 85]

# for name, score in zip(names, scores):
#     print(f' {name} ,{score}')


#     # unzippeed 

# zipped2 = [(1, 'a'), (2, 'b')]
# unzipped = list(zip(*zipped2))
# print(unzipped)



# # practcial implementation 
# keys = ['name', 'age']
# values = ['alice ', 25]
# dicti = dict(zip(keys, values))
# print(dicti)


# # l1 = [1, 2, 3, 4, 5]
# # l2 = [9, 8, 7, 6, 5]
# # comb=list(zip(l1,l2))
# # print(comb)



# l3 = [(1, 9), (2, 8), (3, 7), (4, 6), (5, 5)]
# uncomb= list(zip(*l3))
# print(uncomb)



# l1, l2 = list(zip(*l3))
# print(f"list1 ={l1}")
# print(f"list2 ={l2}")


# print(tuple(l1))
# print(tuple(l2))




l1 = [1, 100, 5, 7]
l2 = [2, 4, 2, 8]

new_list = []

for pair in zip(l1, l2):
    new_list.append(max(pair))
print(new_list)