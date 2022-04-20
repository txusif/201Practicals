# Practical 05
# Linear Search

def linearSearch(arr, n, k):
   for i in range(0,n):
      if arr[i] == k:
         return i
   return -1

arr = [1,3,5,7,8]
k = 7
n = len(arr)
result = linearSearch(arr, n, k)
if result==-1:
    print("Element not found")
else:
    print("Element found at index ",result)