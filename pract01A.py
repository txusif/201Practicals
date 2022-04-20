# Practical 01      Date: 01-02-2022
# Matrix Multiplication 3x4

x = [[3, 3 , 2],
     [1, 4, 8],
     [3, 1, 2]]

# Matrix Y 3x4
y = [[3, 4, 1, 2],
     [1, 6, 2, 1],
     [1, 2, 3, 2]]

#Result matrix 3x4
result = [[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]]

# iterate through rows of x
for i in range(len(x)):
    # iterate through columns of y
    for j in range(len(y[0])):
        # iterate through rows of y
                   for k in range(len(y)):
                           result [i] [j] += x[i][k] * y [k][j]

print("Matrix X")
for r in x:
                   print(r)

print(" ")
print("Matrix Y")
for r in y:
                   print(r)

print(" ")
print("Result X*Y")
for r in result:
                   print(r)