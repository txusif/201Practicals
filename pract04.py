# Practical 04
# Bubble Sort

print("Bubble Sort")
def bubbleSort(list):
    for i in range(0,len(list)):
        for j in range(len(list)-i-1):
            if list[j] > list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
    return list

list = [5, 3, 8, 6, 7, 2]

print("Unsorted list: ",list)
print("Sorted list: ",bubbleSort(list))

#_____________________________________________________________
# Insertion Sort

print("Insertion Sort") 
def insertionSort(list1):  
        for i in range(1, len(list1)):
            value = list1[i]
            j = i - 1
            while j >= 0 and value < list1[j]:
                list1[j + 1] = list1[j]
                j -= 1
            list1[j+1] = value
        return list1
  
list1 = [10, 5, 13, 8, 2]

print("The unsorted list is: ",list1)  
print("The sorted list1 is: ",insertionSort(list1))