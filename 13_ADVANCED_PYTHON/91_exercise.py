# # word counter


# def word_counter(s):
#     count = {}
#     for char in s:
#         count[char] = s.count(char)
#     return count

# print(word_counter("bhushan"))



def word_cont(s):
    count = {}
    for i in s:
        count[i] = s.count(i)
    return count


print(word_cont('siddhi'))