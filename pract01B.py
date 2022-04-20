# Practical 01      Date: 01-02-2022
# Matrix Addition 3x3

x = [[1,2,3],
     [4,5,6],
     [7,8,4]]

# Matrix Y 3x3
y = [[4,3,2],
     [1,0,-1],
     [-2,-3,1]]

#Result matrix 3x3
result = [[0,0,0],
	      [0,0,0],
	      [0,0,0]]

# iterate through rows
for i in range(len(x)):
# iterate through columns
	for j in range(len(x[0])):
		result[i][j] = x[i][j] + y[i][j]

print(" ")
print("Matrix X")
for r in x:
    print(r)

print(" ")
print("Matrix Y")
for r in y:
    print(r)

print(" ")
print("Result Matrix X+Y")
for r in result:
	print(r)
