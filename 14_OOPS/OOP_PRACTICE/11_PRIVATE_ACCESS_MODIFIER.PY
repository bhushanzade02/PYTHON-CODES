class Geek :
    __name = None
    __roll = None
    __branch = None
    
    def __init__(self,name,roll,branch):
        self.__name = name
        self.__roll = roll
        self.__branch = branch
        
    def __displaydetails(self):
        print("name: ", self.__name)
        print("Roll: ",self.__roll)
        print("BRanch: ",self.__branch)
        
    def accessprivatefunction(self):
        self.__displaydetails()
        
obj = Geek("R2J",18303,"it")
print(dir(obj))
print("")

print(obj._Geek__name)
print(obj._Geek__roll)
print(obj._Geek__branch)

print("")

obj.accessprivatefunction()



