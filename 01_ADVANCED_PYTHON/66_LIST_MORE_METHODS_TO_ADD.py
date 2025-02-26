#   INSERT 


fruits1= ['apple', 'mango','banana']
fruits1.insert(1, "hello")

print(fruits1)





#JOIN(CONCATENATE) TWO LIST

fruits2 = ['ornage', 'banana']


fruits = fruits1 + fruits2
print(fruits)



# fruits1.append(fruits2)
# print(fruits1)
 
 #output 

#['apple', 'hello', 'mango', 'banana', ['ornage', 'banana']]



# extend()


fruits1.extend(fruits2)

print(fruits1)