n = int(input())
matrix = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if j > i < n - 1 - j or j < i < n - 1 - j:
            matrix[i][j] = 0
        elif j < i > n - 1 - j or j >= i > n - 1 - j:
            matrix[i][j] = 2
        elif i == n - 1 - j:
            matrix[i][j] = 1
for i in range(n):
    print(*matrix[i])
