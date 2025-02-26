# age=int(input("enter your age "))


# if age >= 1 and age <= 3:
#     print("free")
# elif age >= 4 and age <= 10:
#     print("150 rupees ")
# elif age >= 11 and age <= 60:
#     print("250 rupess")
# else:
#     print("200 rupees")




age = int(input("Please enter your age "))
if age == 0 or age < 0:
    print("you cant watch")
elif 0 < age <= 3:
    print("free")
elif 3 < age <= 10:
    print("150")
elif 10 < age <= 60:
    print("250")
else:
    print("200")