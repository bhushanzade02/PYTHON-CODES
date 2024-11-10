"""Factorial Calculation: Write a Python function that uses a for loop to calculate the factorial of a given number.

"""

result=1
num=int(input("enter a number"))
for num in range(1,num+1):
  result=result*num
print(result)