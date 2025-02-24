class Person: 
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age=age
    def full_name(self):
        return f"{self.first_name}{self.last_name}"

p1 = Person('bhushan', 'zade', 22)
p2 = Person('sid', 'zade', 21)


print(p2.full_name())
