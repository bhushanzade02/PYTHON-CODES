# # # # student = {'name':'bhushan','age':22,'roll_no':28,'address':'hingna'}

# # # # # print(student['age'])
# # # # d1 = {'GFG' : 1, 'Google' : 2, 'GFG1' : 3} 
# # # # print(d1['GFG'])
# # # # for i in student:
# # # #     print(i,student[i])
    
    
# # # # for i in student.keys():
# # # #     print(i)
    


# # # # for i, j in student.items():
# # # #     print(i , j)
    
# # # # print(student.get("age"))

# # # # a = student.items()
# # # # print(a)

# # # # b = student.values()
# # # # c = student.keys()

# # # # print(b,"\n")
# # # # print(c,"\n")


# # # # nest = {1:{"name":'bhushan','age':21,'gender':'male'},2:{"name":'satyam','age':20,'gender':'male'},3:{"name":'sayali','age':9,'gender':'female'}}

# # # # nest["bhush"] = "hello"
# # # # print(nest)

# # # # c = nest[1]["age"]
# # # # c
# # # # print(c)
# # # # print(nest[3]['gender'])



# # # # print(sorted(nest.items()))



# # # # a ={}
# # # # for i in range(1,16):
# # # #     a[i]  = i**2
    
# # # # print( a )


# # # # fp


# # # # d = dict() 
# # # # for x in enumerate(range(2)): 
# # # # 	d[x[0]] = x[1] 
# # # # 	d[x[1]+7] = x[0] 
# # # # print(d) 

# # # # d = {} 

# # # # def addTodict(country): 
# # # # 	if country in d: 
# # # # 		d[country] += 1
# # # # 	else: 
     
# # # # 		d[country] = 1

# # # # addTodict('China') 
# # # # addTodict('Japan') 
# # # # addTodict('china') 

# # # # print (len(d))

# # # # a =dict()

# # # # a[1]=1
# # # # print(a)
# # # # a['1']= "bhus"

# # # # print(a)


# # # # d1 = {"john":40, "peter":45} 
# # # # d2 = {"john":466, "peter":45} 
# # # # print (d1 > d2)


# # # # d = {'GFG' : 'geeksforgeeks.org', 
# # # # 			'google' : 'google.com', 
# # # # 			'facebook' : 'facebook.com'
# # # # 			} 
# # # # del d['google']; 
# # # # for key, values in d.items(): 
# # # # 	print(key, end=" ") 
# # # # d.clear(); 
# # # # for key, values in d.items(): 
# # # # 	print(key) 
# # # # del d; 
# # # # for key, values in d.items(): 
# # # # 	print(key)

# # # # a = {'geeks' : 1, 'gfg' : 2} 
# # # # # b = {'geeks' : 2, 'gfg' : 1} 
# # # # # print (a == b)


# # # # # a = {} 
# # # # # a.fromkeys(['a', 'b', 'c', 'd'], 98) 
# # # # # print (a)
# # # # d = {1 : [1, 2, 3], 2: (4, 6, 8)} 
# # # # d[1]=9
# # # # # print(d)


# # # # d = {1 : {'A' : {1 : "A"}, 2 : "B"}, 3 :"C", 'B' : "D", "D": 'E'} 
# # # # print(d[d[d[1][2]]], end = " ") 
# # # # print(d[d[1]["A"][2]])

# # # # d = {1 : 1, 2 : '2', '1' : 1, '2' : 3} 
# # # # d['1'] = 2
# # # # print(d[d[d[str(d[1])]]])


# # # tup = {}


# # # tup[(1,2,4)] =8
# # # tup[(4,2,1)] =10
# # # tup[(1,2)] =12

# # # print(tup)



# # # tup = (1,2,3)
# # # print(2 * tup)

# # # tup = 2e-04
# # # a = True

# # # print(int(a))
# # # print(int(tup))


# # # a = dict()
# # # b = tuple()
# # # c = set()
# # # d = None
# # # print(type(a),type(b),type(c),type(d))


# # # a= {1,2,3,4,5}
# # # a.add(333)
# # # a.remove(1)
# # # print((a))

# # # a.update([2,3,4,4444])
# # # print(a)



# # # set = {'geeks ','for','gea'}
# # # for i in set:
# # #     print(i)
# # # print(type(set))



# # # set1 = {1, 2, 3} 
# # # set2 = set1.add(4) 
# # # print(set2)


# # # set1 = {1, 2, 3} 
# # # set2 = {4, 5, 6} 
# # # print(len(set1 )+len(set2))

# # # set1 = {0, 2, 4, 6, 8}; 
# # # set2 = {1, 2, 3, 4, 5}; 

# # # print(set1 | set2)


# # # set1 = {0, 2, 4, 6, 8}; 
# # # set2 = {1, 2, 3, 4, 5}; 


# # # print(set1 & set2)




# # # def add( x , y ):
# # #     return x + y



# # # print(add(999,1)) 



# # # def hello(*name):
# # #     print("hello my name is ",name[2])
    
# # # hello("bhushan",'sanjay','zade')


# # # def fact(n):
# # #     if n == 1:
# # #         return 1 
# # #     else :
# # #         return n * fact((n-1))


# # # print(fact(5))



# # # def sq(x):
# # #     return x ** 2 

# # # a =lambda x : x**2

# # # print(sq(4))
# # # print(a(4))

# # # print(type(type(int)))

# # print(chr(ord('A')))

# import datetime

# # x = datetime.datetime.now()
# # print(x)


# y = datetime.datetime(1997,10 ,14)
# # print(y.strftime("%A"))

# import numpy as np


# baked_food = [200,300,400,500,130,302,280,170]


# a = np.array(baked_food)

# print(np.mean(a))
# print(stats.mode(a))

# import numpy as np

# a = np.arange(1, 15)

# print(a)

import pandas as pd
data = {'Name':['punam ','arohi ','pari '],'age':[2,3,4],'salary':[None,45000,25000]}


df = pd.DataFrame(data)

print(df.fillna(method = "bfill "))