n = int(input())
matrix = []
chars = [[0] * n for _ in range(n)]
for i in range(n):
    matrix.append(input().split(' '))
for i in range(n):
    for j in range(n):
        chars[i][j] = matrix[j][i]
for i in range(n):
    print(*chars[i])
