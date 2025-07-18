nums = [1,2,7,1,9,3]

def insertion_sort(arr):
    n= len(arr)
    
    for i in range(1,n):
        curr = arr[i]
        prev = i - 1
        while ( prev >= 0 and arr[prev] > curr):
            arr[prev+1] = arr[prev]
            prev -=1
        arr[prev+1] = curr
    return arr

print(insertion_sort(nums))
    
    
    
    