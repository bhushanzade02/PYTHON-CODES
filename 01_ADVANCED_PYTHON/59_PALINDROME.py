# name = "naman"



# for i in name:
#     ans = name[::-1]
# if name[::-1] == name:
#     print("it is a palindrome")
# else:
#     print("it is not")




def i_palindrome(word):
    if word == word[::-1]:
        return True
    return False





print(i_palindrome("bhushan"))
print(i_palindrome("naman"))