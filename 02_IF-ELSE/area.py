from test.test_unparse import elif1

print("***AREA CALUCLATOR*****")

print("press 1 to 4 keys for different types of operation given beloe "
      "\n pres 1 for sqaure "
      "\n press 2 or rectangle"
      " \n press 3 for  radius of cicrcle "
      "\n press 4 for area of triagnle")

choice=int(input("enter a number "))

if choice==1:
   side= int(input('enter a side'))
   area=side**2
   print(area)

elif choice == 2:
    l=float(input("enetr e length"))
    b=float(input("enter breadth"))
    area=l*b
    print(area)

elif choice==3:
    radius=float(input("enter a radius"))
    area=3.14*(radius**2)
    print(area)

elif choice==4:
        base=float(input("enter a base"))
        height=float(input("enter a height"))
        area=0.5*base*height
        print(area)
else:
    print("invalid enter")

print("thank you")
