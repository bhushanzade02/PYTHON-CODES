nums=[34,2,-34,5,43]

start=0
end=len(nums)-1
while(start<end):
    nums[start],nums[end]=nums[end],nums[start]
    start+=1
    end-=1
print(nums) #reverse