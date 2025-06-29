nums=[1,2,3,4,5,6]
target = 3
def pair_sum(nums):
    n= len(nums)
    i=0 
    j=n-1
    while(i<j):
        ps=nums[i]+nums[j]
        if ps==target:
            return [i,j]
        elif (ps>target):
            j-=1
        else:
            i+=1


print(pair_sum(nums))
