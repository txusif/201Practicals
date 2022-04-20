# Practical 02      Date: 15-02-2022

# Sum of elements of an Array
# Initialize an Array
arr = [1, 2, 3, 4, 5]
sum = 0
# Loop through the array to calculate sum of elements
for i in range(0, len(arr)):
    sum = sum + arr[i]
print("Sum of all the elements of an array: "+str(sum))