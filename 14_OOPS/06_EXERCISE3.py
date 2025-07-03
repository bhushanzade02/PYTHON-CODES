class Person:
    count=0
    def __init__(self,first_name,last_name,age):
        Person.count+= 1
        self.first_name = first_name;
        self.last_name = last_name
        self.age = age
p1=Person('bhushan','zade',24)
p2=Person('bhu3s3han','zeade',24)
p3=Person('bhu3shan','zaede',24)
p4=Person('bh33ushan','zaede',24)
p5=Person('bhus3han','za33de',24)
print(Person.count)




# every time you make objects construtor is called 

        
        