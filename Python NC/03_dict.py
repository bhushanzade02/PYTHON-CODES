dic = {'name' : "mangesh", 'age' : 21, 'city': ''}


# print(dic.get("name"))   
# print(dic.get("city", "Pune"))  
# print(dic)



d = {'a': 1, 'b': 2}
d.clear()
print(d)  


d = {'a': 1, 'b': 2}
d2 = d.copy()
print(d2)  

d = {'a': 1, 'b': 2}
print(d.get('a')) 
print("this is ",d.get('c')) 
print(d.get('c', 0))    


d = {'a': 1, 'b': 2}
print(d.keys())  

d = {'a': 1, 'b': 2}
print(d.values())  

d = {'a': 1, 'b': 2}
print(d.popitem())  
print(d)        