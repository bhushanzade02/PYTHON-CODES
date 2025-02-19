

numbers = [1, 2, 3, 4, 5]
print(max(numbers))
print(min(numbers))





def func(iten):
    return len(iten)

names = ['Harshit', 'Bhushan', 'sid','ab']
print(max(names, key=func))
print(min(names, key=func))



#now using lambda function 
names = ['Harshit', 'Bhushan', 'sid','ab']
print(max(names, key=lambda item: len(item)))
print(min(names,key=lambda item : len(item)))



# now for list

student2 = [
    {'name': "harsh", 'score': 90, 'age': 24},
    {'name': "mohit", 'score': 70, 'age': 19},
    {'name':'rohit','score':60,'age':27}
]


print(max(student2, key =lambda item:item.get('score'))['name'])
print(max(student2, key=lambda item: item.get('age'))['name'])


# now for dictionary
student1 = {
    'harshit': {'score': 90, 'age': 24},
    'mohit': {'score': 75, 'age': 19},
    'rohit':{'score':76,'age':23}
}


print(max(student1,key=lambda item : student1[item]['score']))