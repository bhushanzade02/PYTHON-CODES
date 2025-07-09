vowels = ['a','e','i','o','u']
word = 'bhushan'
count =0 
for char in word:
    if char not in vowels:
        count +=1
print(count)

        