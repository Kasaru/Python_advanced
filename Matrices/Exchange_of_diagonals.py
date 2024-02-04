n = int(input())
matrix = []
chars = []
for k in range(n):
    matrix.append(input().split(' '))
for i in range(n):
    for j in range(n):
        if i == j:
            matrix[i][j], matrix[n - i - 1][j] = matrix[n - i - 1][j], matrix[i][j]
for i in range(n):
    print(*matrix[i])
