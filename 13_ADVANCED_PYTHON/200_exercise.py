def to_power(num, *args):
    if args:
        return [i ** num for i in args]
    else:
        return 'you diidnt pass any args '

nums = [1, 2, 3]

print(to_power(2, *nums))

print(to_power(3,*[2,3]))





# TO CHECK WHETHER THE THE STRING IS EMPTY OR NOT 
# l=[1,2,3,5,6]
# if l:
#     print('not empyty')
# else:
#     print('empty')