vowels = ['a','e','i','o','u']

word = 'bhushanSanjayZade'
count = 0 
for i, ch in enumerate(word.lower()):
    if ch in vowels:
        count+=1

print(count)



