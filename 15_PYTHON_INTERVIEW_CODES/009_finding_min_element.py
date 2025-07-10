nums=[1,12,3,4,31,11,13,4,31,44,]
min = nums[0]
for num in nums:
    if min > num:
        min = num
print(min)