word = 'Bhushansanjayzade'
vowels = ['a','e','i','o','u']


count = 0 
for i in word :
    if i not in vowels :
        count+=1
print(count)
print(len(word)-6)