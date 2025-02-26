class Person:
    count_instance = 0  # Class variable to count instances

    def __init__(self, first_name, last_name, age):  # Fixed `__init__`
        Person.count_instance += 1  # Increment instance count
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    @classmethod
    def count_instances(cls):  # Class method
        return f"You have created {cls.count_instance} instances of {cls.__name__}"

    def full_name(self):  # Instance method
        return f"{self.first_name} {self.last_name}"  # Added space

    def is_above_18(self):  # Instance method
        return self.age > 18


p1 = Person("Bhushan", "Zade", 22)
p2 = Person("Siddhi", "Zade", 22)

print(Person.count_instances())  # Now correctly calls the class method
