n, m = input().split(' ')
n, m = int(n), int(m)
matrix1 = []
matrix2 = []
result = [[0] * m for _ in range(n)]
for i in range(n):
    matrix1.append(input().split(' '))
input()
for i in range(n):
    matrix2.append(input().split(' '))
for i in range(n):
    for j in range(m):
        result[i][j] = int(matrix1[i][j]) + int(matrix2[i][j])
for i in range(n):
    print(*result[i])
