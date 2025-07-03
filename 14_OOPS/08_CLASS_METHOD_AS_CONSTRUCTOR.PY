class Person:
    count_instance = 0
    
    def __init__(self, first_name, last_name, age):
        Person.count_instance += 1
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        
        
    @classmethod
    def from_string(cls, string):
        first, last, age = string.split(',')
        return cls(first, last, age)

    @classmethod
    def count_instances(cls):
        return f'you have creatde {cls.count_instance} instances of{cls.__name__} '

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def is_above_18(self):
        return self.age>18

p1 = Person("BHushan", "zade", 21)
p2 = Person("Siddhi", "zade", 22)

p3 = Person.from_string('bhushan,zade,22')
print(p3.full_name())
