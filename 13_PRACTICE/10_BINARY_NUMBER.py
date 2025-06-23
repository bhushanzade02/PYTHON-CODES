nums=[1,2,3,4,5]
target = 3


# def binary_search(nums, target):
#     # Step 1: Sort the list (required for binary search)


#     # Step 2: Set starting and ending pointers
#     start = 0
#     end = len(nums) - 1

#     # Step 3: Loop until pointers cross
#     while start <= end:
#         mid = start + (end - start )//2 # Find middle index

#         if nums[mid] == target:
#             return mid  # Target found, return index
#         elif nums[mid] < target:
#             start = mid + 1  # Target is in right half
#         else:
#             end = mid - 1  # Target is in left half

#     return -1  # Target not found


# print(binary_search(nums,target))




# binary serach through recusrion:


def binary_search(nums, target,st , end):
    if (st <= end):
        mid = st +(end - st )//2
        if target < nums[mid] :
            return binary_search(nums , target , st, mid-1)
        elif target > nums[mid] :
            return binary_search(nums , target , mid+1 , end )
        else:
            return mid
    return -1 

st= 0
end = len(nums)-1
print(binary_search(nums,target,st,end))