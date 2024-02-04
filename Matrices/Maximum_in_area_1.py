n = int(input())
matrix = []
chars = []
maximum = -999999
for i in range(n):
    matrix.append(input().split(' '))
for i in range(n):
    for j in range(n):
        if j <= i:
            chars.append(matrix[i][j])
            if maximum < int(matrix[i][j]):
                maximum = int(matrix[i][j])
print(maximum)
