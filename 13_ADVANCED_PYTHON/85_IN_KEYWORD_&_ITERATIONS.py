user_info = {

    'name': 'BHushan',
    'age': 24,
    'fav': ['coco', 'mono'],
    'fav_tunes':['sing','song']
    
}


print(user_info)


if "namee" in user_info:
    print('present')
else:
    print('not present ')
    


if 24 in user_info.values():
    print('present')
else:
    print('not present')




## looping
print(user_info)

# through this only du=ictionaries keys are in this 
for i in user_info:
    print(i)
    

# through this values are print

for i in user_info.values():
    print(i)



user_info_values = user_info.values()
print(user_info_values)



user_info_key = user_info.keys()
print(user_info_key)