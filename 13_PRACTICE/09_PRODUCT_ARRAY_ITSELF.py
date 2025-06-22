nums=[1,2,3,4]



def productA(nums):
        ans=[]
        product=1
        for i in range(len(nums)):
            product*=nums[i]
            i+=1
        for i in range(len(nums)):
            ans.append(product//nums[i])
        return ans

print(productA(nums))