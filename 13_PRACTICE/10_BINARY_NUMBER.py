nums=[1,2,3,4,5]
target = 3

def binary_search(nums, target):
    # Step 1: Sort the list (required for binary search)


    # Step 2: Set starting and ending pointers
    start = 0
    end = len(nums) - 1

    # Step 3: Loop until pointers cross
    while start <= end:
        mid = (start + end) // 2  # Find middle index

        if nums[mid] == target:
            return mid  # Target found, return index
        elif nums[mid] < target:
            start = mid + 1  # Target is in right half
        else:
            end = mid - 1  # Target is in left half

    return -1  # Target not found


print(binary_search(nums,target))