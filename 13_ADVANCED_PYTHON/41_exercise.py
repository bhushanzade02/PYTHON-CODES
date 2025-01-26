# probelm
# ask to user to input a number conatining more than one digit
# example 1256
# calculate 1 + 2 + 5 + 6




number = input("enter a number")
i = 0
sum = 0
while i < len(number):
    sum += int(number[i])
    i += 1
print(sum)
    
