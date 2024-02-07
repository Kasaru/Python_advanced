n = int(input())
matrix = []
chars = []
maximum = -999999
for i in range(n):
    matrix.append(input().split(' '))
for i in range(n):
    for j in range(n):
        if (j >= i >= n - 1 - j ) or (j <= i >= n - 1 - j ):
            chars.append(matrix[i][j])
            if maximum < int(matrix[i][j]):
                maximum = int(matrix[i][j])
print(maximum)
