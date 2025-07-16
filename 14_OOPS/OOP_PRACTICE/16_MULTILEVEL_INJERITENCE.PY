class Base:
    def __init__(self,name , roll, role):
        self.name = name

        self.roll = roll
        self.role = role
        
class Intermediate(Base):
    def __init__(self,name,age, roll,role):
        super().__init__(name, roll,role)
        self.age = age 
        
        
class Derived(Intermediate):
    def __init__(self,name , age , roll , role):
        super().__init__(name , age ,roll , role)
          
    def print_data(self):
        print(f"the name is {self.name}")
        print(f"the age is {self.age}")
        print(f"the roll is {self.roll}")
        print(f"the role is {self.role}")
        
        
obj = Derived("LOKESH SINGH", 21 , 101, "software trainer")
obj.print_data()
        
        
        