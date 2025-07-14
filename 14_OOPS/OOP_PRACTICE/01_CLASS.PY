class Dog:
    species = "Canien" # class Atrribute / class data member
    
    
    def __init__(self,name,age):
        self.name= name   #instance attribute / object data member
        self.age = age
        
    def bark(self):
        print(f'{self.name} is barking')
        
    def __str__(self):
        return f"{self.name} is {self.age} is year old "
    
    
    
dog1 = Dog("Buddy",3)
dog2 = Dog("charlie",5)


#access the classs variable 

print(dog1.species)
print(dog2.species)

print(dog1.name)
print(dog1.age)

print(dog2.name)
print(dog2.age)

# modify the instance variable
dog1.name= "Max"
print(dog1.name)

# modify the class variable 
Dog.species= "Feline"

print(dog1.species)
print(dog2.species)


dog1.bark()

print(dog1)
print(dog2)