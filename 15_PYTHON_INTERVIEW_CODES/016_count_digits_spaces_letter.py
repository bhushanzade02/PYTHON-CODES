import re
name = 'pyhton is  3 2 1 1'
digitCount=re.sub("[^0-9]","", name)
letterCount = re.sub('[^a-zA-z]','',name)
spaces= re.findall('[\s]',name)


print(digitCount)
print(letterCount)
print(spaces)