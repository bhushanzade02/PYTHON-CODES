# wihtout using enumearte function 


names = ['abc', 'abcdef', 'harshit']
# pos = 0
# for name in names:
#     print(f'{pos}----->{name}')
#     pos += 1




# with the help of enumerate function 


for pos, name in enumerate(names):
    print(f'{pos}----> {name}')
    