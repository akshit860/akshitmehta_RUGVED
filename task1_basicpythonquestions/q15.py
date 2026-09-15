n = int(input("Enter the size of matrix: "))

matrix = []

print("Enter the matrix:")

for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)
rotated = []

for j in range(n):
    row = []
    for i in range(n - 1, -1, -1):
        row.append(matrix[i][j])
    rotated.append(row)

print("Rotated matrix:")

for row in rotated:
    print(*row)
print("Spiral order:")

top = 0
bottom = n - 1
left = 0
right = n - 1

while top <= bottom and left <= right:
    for j in range(left, right + 1):
        print(rotated[top][j], end=" ")
    top += 1
    for i in range(top, bottom + 1):
        print(rotated[i][right], end=" ")
    right -= 1
    if top <= bottom:
        for j in range(right, left - 1, -1):
            print(rotated[bottom][j], end=" ")
        bottom -= 1
    if left <= right:
        for i in range(bottom, top - 1, -1):
            print(rotated[i][left], end=" ")
        left += 1