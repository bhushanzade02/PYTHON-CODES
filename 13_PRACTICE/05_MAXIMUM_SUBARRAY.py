nums=[-2,1,-3,4,-1,2,1,-5,4]



def maximumsubarray(nums):
    curr_sum=0
    max_sum= -10**9
    
    for num in nums:
        curr_sum+=num
        max_sum=max(curr_sum,max_sum)
        if curr_sum<0:
            curr_sum=0
    return max_sum
    
    
print(maximumsubarray(nums))