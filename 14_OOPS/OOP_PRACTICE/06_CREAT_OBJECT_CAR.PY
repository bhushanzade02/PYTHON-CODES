class Car:
    def __init__(self,make,model,year):
        self.make=make
        self.model = model
        self.year = year
        self.mileage =0 
        
    def drive(self, distance):
        self.mileage += distance
        
a = Car("toyota ",'Fortuner ',2022)

print(f'{a.make}{a.model}{a.year}')
a.drive(132)
print(f'mileage: {a.mileage} miles')