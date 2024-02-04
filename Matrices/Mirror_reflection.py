n = int(input())
matrix = []
for k in range(n):
    matrix.append(input().split(' '))
for i in range(n // 2):
    for j in range(n):
        matrix[i][j], matrix[n - i - 1][j] = matrix[n - i - 1][j], matrix[i][j]
for i in range(n):
    print(*matrix[i])
