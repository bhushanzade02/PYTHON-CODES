def checkpalindrome(stri):
    if stri == stri[::-1]:
        return "it is a palindrome"
    return 'not a palindrome'


print(checkpalindrome("bhushan"))
print(checkpalindrome("kayak"))