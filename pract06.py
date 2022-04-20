# Practical 06
# Binary Search

def binarySearch(arr, k, low, high): 
    while low <= high:     
        mid = (high + low) // 2  
        if arr[mid] == k:
            return mid 
        elif k < arr[mid]:  
            high = mid - 1  
        else:  
            low = mid + 1 
    return -1  
   
arr = [1, 3, 5, 7, 9]  
k = 1
result = binarySearch(arr, k, 0, len(arr)-1)  
  
if result != -1:  
    print("Element is present at index: ",str(result))  
else:  
    print("Element is not found")  