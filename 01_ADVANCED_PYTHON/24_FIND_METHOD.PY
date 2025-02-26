string = "she is beautiful and she is a good dancer"


print(string.find("is", 1))

## for finding 2 nd is we have to start finding after 1 st is wher yo find 


is_pos1 = string.find("is", 1)
print(string.find("is",is_pos1+1))