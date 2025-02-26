nums = list(range(1, 11))
 
#  if the num is odd then negative and if num is even is multpy it by 2 



new_list = []
for i in nums:
    if i % 2 == 0:
        new_list.append(i * 2)
    else:
        new_list.append(-i)
print(new_list)


new_list2 = [i * 2 if (i % 2 == 0) else - i]
print(new_list)