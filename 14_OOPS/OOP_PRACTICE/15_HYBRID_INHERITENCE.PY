class Animal:
    def speak(self):
        print("animal can speak")
        
class Mammal(Animal):
    def give_birth(self):
        print("mammals give birth")


class Bird(Animal):
    def lay_eggs(self):
        print("Bird lays eggs")
        
class Platypus(Mammal, Bird):
    pass



platypus = Platypus()
platypus.speak()
platypus.give_birth()
platypus.lay_eggs()