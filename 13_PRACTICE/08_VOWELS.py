name  ='bhaeiou'

def find_vowels(name):
    name=str(name)
    vowels= ('a','e','i','o','u')
    ans=''
    for i in name:
        if i in vowels:
            ans+=i
    return ans 
    
print(find_vowels(name))


