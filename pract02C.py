# Practical 02      Date: 15-02-2022
# Finding Maximum and Minimum element in an Array

def MaxMinPosotion(A, n):
    minPosition = A.index(min(A))
    maxPosition = A.index(max(A))
    print("The Minimum value is at postion: ", (minPosition + 1))
    print("The Maximum value is at postion: ", (maxPosition + 1))

A = list()
n = int(input("Enter the size of the list: "))
for i in range(int(n)):
    k = int(input("Enter the elements: "))
    A.append(k)

MaxMinPosotion(A, n)