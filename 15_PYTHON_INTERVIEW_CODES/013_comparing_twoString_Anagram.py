str1= 'li sten'
str2= 'silent'

str1 = str1.replace(" ","").upper()
str2 = str2.replace(" ","").upper()

if sorted(str1) == sorted (str2):
    print(True,"Anangram")
else:
    print(False,"Not a Anagram")