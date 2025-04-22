# Input: three sides of a triangle
# Output: whether a triangle is possible
# Rule: sum of any two sides must be greater than the third


a=int(input("Enter side a "))
b=int(input("Enter side b "))
c=int(input("Enter side c "))



if(a+b>c and a+c>b and b+c >a):
    print("Triangle is Posible")
else:
    print("TRiangle is NOt possible")

