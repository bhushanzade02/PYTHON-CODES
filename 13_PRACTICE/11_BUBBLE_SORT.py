#Bubble sort 
nums=[9,8,7,6,5,4,3,2,1]
def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n):
        iswap= False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                iswap = True
        if not iswap:
            break
    return arr


print(bubble_sort(nums))