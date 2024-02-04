n, m = input().split(' ')
n, m = int(n), int(m)
matrix = [[0] * m for _ in range(n)]
num = 0
for i in range(n):
    for j in range(m):
        num += 1
        matrix[i][j] = str(num).ljust(3)
for i in range(n):
    print(*matrix[i])
