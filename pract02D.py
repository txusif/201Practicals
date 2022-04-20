# Practical 02      Date: 15-02-2022
# Count the number of Even and Odd number

def CountingEvenOdd(arr, arr_size):
	even_count = 0
	odd_count = 0

	for i in range(arr_size):
		if (arr[i] % 2==0):
			even_count += 1
		else:
			odd_count += 1

	print("Number of even elements:", even_count)
	print("Number of odd elements:", odd_count)

arr = [2, 3, 4, 5, 6]
n = len(arr)

CountingEvenOdd(arr, n)