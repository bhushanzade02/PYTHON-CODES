win_num = 9
guss_num = int(input('enter a number'))
if guss_num == 9:
    print("win")
else:
    if guss_num < win_num:
        print('low num')
    else:
        print("high num")