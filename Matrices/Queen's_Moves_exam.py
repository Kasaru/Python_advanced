xy = input()
matrix = [['.'] * 8 for _ in range(8)]
x = 'abcdefgh'.index(xy[0])
y = '87654321'.index(xy[1])
matrix[y][x] = 'Q'
for i in range(8):
    for j in range(8):
        if (i == y and j != x) or (j == x and i != y) or (x + i == y + j and i != y and j != x) or (
                abs(x - j) == abs(y - i) and i != y and j != x):
            matrix[i][j] = '*'
for i in range(8):
    print(*matrix[i])
