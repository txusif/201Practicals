# Practical 01      Date: 15-02-2022
# Row and Column sum

a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

rows = len(a)
cols = len(a[0])

# calculate sum of each row of given matrix
print("Row Addition")
for i in range(0, rows):
    sumRow = 0
    for j in range(0, cols):
        sumRow = sumRow + a[i][j]
    print("Sum of "+str(i+1)+" row: "+str(sumRow))


# calculate sum of each column of given matrix
print(" ")
print("Column Addition")
for i in range(0, rows):
    sumCol = 0
    for j in range(0, cols):
        sumCol = sumCol + a[j][i]
    print("Sum of "+str(i+1)+" column: "+str(sumCol))