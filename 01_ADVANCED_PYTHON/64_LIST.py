num = [1, 2, 3, 45, 3]
print(num)


words = ['word1', 'word2', 'word3', 'word4']
print(words)




mixed = [1, 2, 3, "hello", 'this', 2.3, 4.4]
print(mixed)


mixed[1] = "bhushan"


print(mixed)



mixed[1:] = 'thre'


print(mixed)

# OUTPUT: -
# [1, 2, 3, 45, 3]
# ['word1', 'word2', 'word3', 'word4']
# [1, 2, 3, 'hello', 'this', 2.3, 4.4]
# [1, 'bhushan', 3, 'hello', 'this', 2.3, 4.4]
# [1, 't', 'h', 'r', 'e']
