n, m = int(input()), int(input())
matrix = []
chars = []
coordinates = []
maximum = -999999
for i in range(n):
    matrix.append(input().split(' '))
for i in range(n):
    for j in range(m):
        chars.append(matrix[i][j])
        if maximum < int(matrix[i][j]):
            coordinates = []
            maximum = int(matrix[i][j])
            coordinates.append(i)
            coordinates.append(j)
print(*coordinates)
