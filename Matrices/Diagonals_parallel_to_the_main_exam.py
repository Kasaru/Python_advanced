n = int(input())
matrix = [[0] * n for _ in range(n)]
for k in range(n):
    for i in range(n):
        for j in range(n):
            matrix[i][j] = abs(i - j)
for i in range(n):
    print(*matrix[i])
