nums=[1,1,2,2,5,3,5]



def single_num(nums):
    for i in range(len(nums)):
        count=0
        for j in range(len(nums)):
            if nums[i]==nums[j]:
                count+=1
        if count==1:
            return nums[i]
            
            
print(single_num(nums))