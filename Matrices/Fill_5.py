n, m = input().split(' ')
n, m = int(n), int(m)
matrix = [[f'{m}'.ljust(3)] * m for _ in range(n)]
for i in range(n):
    num = 0
    for j in range(m):
        num = (i + j + 1) % m
        if num != 0:
            matrix[i][j] = str(num).ljust(3)
for i in range(n):
    print(*matrix[i])
