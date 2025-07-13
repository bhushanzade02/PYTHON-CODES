# import string
# exclude = string.punctuation
# print(exclude)


def count_sp_char(string):
    sp_char= "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
    count =0 
    for i in string:
        if i in sp_char:
            count+=1
    return count

string = "Hehlloo ! hi , I am Bhushan.."
print(count_sp_char(string ))