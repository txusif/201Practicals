# Practical 02      Date: 15-02-2022
#  Searching an element in an Array

def linearSearch(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return "Element not found"
arr = ("jc", "jw", "kc", "tx", "ye")
x = "tx"
print("Element found at index: "+str(linearSearch(arr, x)))