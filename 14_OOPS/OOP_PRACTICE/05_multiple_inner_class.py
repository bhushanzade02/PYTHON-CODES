
class Doctors:
    def __init__(self):
        self.name = 'Doctor'
        self.den = self.Dentist()
        self.car = self.Cardiologist()

    def show(self):
        print('In outer class')
        print('Name:', self.name)


    class Dentist:
        def __init__(self):
            self.name = 'Dr. SID'
            self.degree = 'BDS'

        def display(self):
            print("Name:", self.name)
            print("Degree:", self.degree)

    class Cardiologist:
        def __init__(self):
            self.name = 'Dr. BHUS'
            self.degree = 'DM'

        def display(self):
            print("Name:", self.name)
            print("Degree:", self.degree)


outer = Doctors()
outer.show()

d1 = outer.den

d2 = outer.car
print()
d1.display()
print()
d2.display()