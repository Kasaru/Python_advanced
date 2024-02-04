xy = input()
matrix = [['.'] * 8 for _ in range(8)]
x = 'abcdefgh'.index(xy[0])
y = '87654321'.index(xy[1])
matrix[y][x] = 'N'
for i in range(8):
    for j in range(8):
        if (x - j) * (y - i) == 2 or (x - j) * (y - i) == -2:
            matrix[i][j] = '*'
for i in range(8):
    print(*matrix[i])
