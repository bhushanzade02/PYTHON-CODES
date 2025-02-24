# class Circle:
#     def __init__(self, radius, pi):
#         self.radius = radius
#         self.pi = pi
#     def cal_circumference(self):
#         return 2 * self.pi * self.radius
          

# c1 = Circle(4,3.14)
# c2 = Circle(3, 3.14)
# print(c1.cal_circumference())


class Circle:
    pi=3.14 # <--------------- Insead of writing again and again we declare the pi variabale at atop called as class varible 
    def __init__(self, radius, pi):
        self.radius = radius
    def cal_circumference(self):
        return 2 * pi * self.radius
        

c1 = Circle(4)
c2 = Circle(3)


print
