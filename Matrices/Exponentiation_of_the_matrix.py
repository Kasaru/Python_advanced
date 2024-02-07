n = int(input())
matrix1 = []
matrix2 = []
e = 0
for i in range(n):
    matrix1.append(input().split(' '))
matrix2 = matrix1
ex = int(input())
result = [[0] * n for _ in range(n)]
for e in range(ex - 1):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += int(matrix1[i][k]) * int(matrix2[k][j])
    if e < ex - 2:
        matrix2 = result
        result = [[0] * n for _ in range(n)]
for i in range(n):
    print(*result[i])
