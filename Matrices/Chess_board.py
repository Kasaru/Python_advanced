n, m = input().split(' ')
n, m = int(n), int(m)
matrix = [['.'] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if (i % 2 == 0 and j % 2 == 1) or (i % 2 == 1 and j % 2 == 0):
            matrix[i][j] = '*'
for i in range(n):
    print(*matrix[i])
