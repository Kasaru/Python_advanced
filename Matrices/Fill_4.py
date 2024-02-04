n = int(input())
matrix = [['0'.ljust(3)] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if (i == j or i == n - j - 1) or (j > i < n - 1 - j) or (j < i > n - 1 - j):
            matrix[i][j] = '1'.ljust(3)
for i in range(n):
    print(*matrix[i])
