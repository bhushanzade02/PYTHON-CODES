nums=[34,2,-34,5,43]
def returnindices(x):
    smallest=10**9
    for i in range(len(x)):
        if x[i]<smallest:
            smallest=nums[i]
    for i in range(len(x)):
        if x[i]==smallest:
            return i
print(returnindices(nums))
