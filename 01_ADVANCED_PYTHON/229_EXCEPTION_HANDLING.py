#Exception Handling


while True:
    try:
        age = int(input("Enter your age:"))
        break
    except ValueError:
        print('oops you enterd string.. try Again')
    except:
        print("Unexpected Error")
    
if age > 18:
    print("you are eligible")
else:
    print("you are noteligible")
