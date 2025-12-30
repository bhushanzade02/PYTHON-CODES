def CountWhiteSpace(n):
    count =0 
    for i in n:
        if  i == " ":
            count+=1
    return count

mystring = "this line conatin four whitespces"

print(CountWhiteSpace(mystring))

