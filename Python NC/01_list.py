# name  = ['satyam','rahul', 'satyam']
# person = ['Mangesh',21,5.8,True]


# print(len(name))
# print(name.append('hello')) 
# print(name)#list.append(item)
# print(name.remove('rahul'))
# print(name) #list.remove(value)
# print(name.reverse)
# print(name)
# print(name.count('satyam'))  #list.count(value)
# print(name)
# print(name.clear())
# print(name)


name = ["rahul", "satyam", "amit", "hello"]
print(name.__getitem__(2))  

name = ["rahul", "satyam", "amit"]
name.__setitem__(1, "vikas")   
print(name)  

name = ["rahul", "satyam", "amit"]
name.__delitem__(0)   
print(name)

name = ["rahul", "satyam"]
print(name.__mul__(3))   

name = ["rahul", "satyam", "amit"]
print(name.__contains__("amit"))   
print(name.__contains__("arjun"))  
