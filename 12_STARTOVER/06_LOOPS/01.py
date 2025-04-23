# for i in range(1,11):
#     print("HEllO World")

# n=2
# for i in range(1,11):
#     print(n,"X",i,"=",n*i)


#sum of 1 to n number




# # print numbers from 1 to n 
# for i in range(1,11):
#     print(i)
#     print("")




#  2. Sum of First N Natural Numbers

# n =int(input("Enter a NUmber"))
# sum =0 
# for i in range(1,n+1):
#     sum+=i
    
    
# print(sum)



# 3. Factorial of a Number


# num=int(input("enter a number"))

# fact=1

# for i in range(1,num+1):
#        fact=fact*i
       
# print(fact)

        
        
#  4. Reverse a Number

# # Input: 1234
# # Output: 4321


# num="1234"
 
 
 



# print(num[::-1])




#   
# num=(input("ENter a numebr"))
# sum=0
# for i in range(0,len(num)):
#     sum+=int(num[i])  
# print(sum)




# n=1

# while n<=5:
#     print(n)
#     n+=1


# sum =0
# i=1
# n = int(input("Enter a number "))


# while i <=n:
#     sum+=i
#     i+=1
# print(sum)


# sum =0
# n ="110"

# for i in range(0,len(n)):
#     sum+=int(n[i])
    
# print(sum)

# n="121"
# sum=0 
# i=0
# while i<len(n):
#     sum+=int(n[i])
#     i+=1
# print(sum)




# num = int(input("Enter a number: "))
# reverse = 0

# while num > 0:
#     digit = num % 10         # get last digit
#     reverse = reverse * 10 + digit  # build reversed number
#     num = num // 10          # remove last digit

# print("Reversed number:", reverse)






# num= int(input("enter a number"))
# rev=0


# while num>0:
#     digit =num%10
#     rev=rev*10+digit
#     num=num//10
# print(rev)
    
    
# while True:
#     name=input("enter a name")
#     if name == "exit":
#         break
#     print("hello ",name)



# while True:
#     num1=7
#     num2=3
#     print(num1+num2)
#     break



# for i in range(3):
#     for j in range(3):
#         print(i,j)


# rows=int(input("Enter a values "))
# cols=int(input("Enter a values "))

# matrix=[]


# for i in range(rows):
#     row=[]
#     for j in range(cols):
#         val=int(input("ENter a value"))
#         row.append(val)
#     matrix.append(row)
        
    
    
# print("\n   your Matrix is ")
# for i in range( rows):
#     for j in range(cols):
#             print(matrix[i][j],     end=" ")
#     print()



# for i in range(1,4):
#     for j in range(1,4):
#         print(j)
# print()



# for i in range(1,11):
#     print(i)




# for i in range(10):
#     if i==5:
#         break
#     print(i)



# for i in range(1,11):
#     if i==5:
#         continue
#     print(i)



# #even
# n=int(input("ENter a NUmber"))



# for i in range(1,n+1):
#     if i%2!=0:
#          print(i,end=" ")




# for i in range(1,10):
#     if i==3:
#         print("THIS IS MY FAV SONG")
#     else:
#         print(i)


# for i in range(1,100):
#     if i%8==0 and i%12==0:
#         print(i)


# n=1

# while(n<=10):
#     if n==4:
#         print("this is my fav osng")
#     else:
#         print(n)
#         n+=1





# sum=0
# for i in range(1,7):
#     if i%2==0:
#         sum+=i
# print(sum)