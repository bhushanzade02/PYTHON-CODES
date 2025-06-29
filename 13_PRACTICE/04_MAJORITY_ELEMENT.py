nums=(
    [3]*4+[2]*100
)


def majorityelement(nums):
    nums.sort()
    n=len(nums)
    freq=1
    for i in range(1,n):
        if nums[i]==nums[i-1]:
            freq+=1
        else:
            freq=1
        if freq>n//2:
            return nums[i]




print(majorityelement(nums))