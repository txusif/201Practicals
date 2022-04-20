# Practical 07
# Kth smallest value

def Kth_smallest_element(list, n, k):
    list.sort()
    return list[k-1]

list=[]
n = int(input("Enter the length of array: "))
for i in range(int(n)):
    ele=int(input("Enter the element: "))
    list.append(ele)
k = int(input("Enter Kth value: "))

print("Kth smallest value is: ",Kth_smallest_element(list, n, k))