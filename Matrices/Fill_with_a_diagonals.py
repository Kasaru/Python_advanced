n, m = input().split(' ')
n, m = int(n), int(m)
matrix = [[f'{m}'.ljust(3)] * m for _ in range(n)]
num = 1
i = 0
for c in range(n + m - 1):
    for i in range(n):
        for j in range(m):
            if i + j == c:
                matrix[i][j] = str(num).ljust(3)
                num += 1
for i in range(n):
    print(*matrix[i])
