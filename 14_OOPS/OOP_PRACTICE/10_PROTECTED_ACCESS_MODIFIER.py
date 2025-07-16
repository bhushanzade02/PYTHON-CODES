class Student:
    _name = None
    _name = None
    _branch = None
        
    def __init__(self,name,roll,branch):
        self.name = name
        self.roll = roll
        self.branch = branch
        
    def _displayrollandbranch(self):
        print("Roll no ", self.roll)
        print("branch ", self.branch)
        
class Geek(Student):
    def __init__(self ,name,roll,branch):
        Student.__init__(self,name,roll,branch)
    
    
    def displayDetails(self):
        print('Name: ',self._name)
        self._displayrollandbranch()
        
        
stu = Student("Alpha",12345,"Computer Science")
print(dir(stu))



print(stu._name)
stu._displayrollandbranch()




obj = Geek("Raj",123456,"Information Technology")
print("")
print(dir(obj))


obj.displayDetails