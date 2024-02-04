n, m = input().split(' ')
n, m = int(n), int(m)
matrix = [[f'{m}'.ljust(3)] * m for _ in range(n)]
num = 0
for i in range(n):
    for j in range(m):
        num += 1
        if i % 2 != 0:
            matrix[i][m - j - 1] = str(num).ljust(3)
        else:
            matrix[i][j] = str(num).ljust(3)
for i in range(n):
    print(*matrix[i])
