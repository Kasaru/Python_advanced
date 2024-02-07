n1, m1 = input().split(' ')
n1, m1 = int(n1), int(m1)
matrix1 = []
matrix2 = []
for i in range(n1):
    matrix1.append(input().split(' '))
input()
n2, m2 = input().split(' ')
n2, m2 = int(n2), int(m2)
for i in range(n2):
    matrix2.append(input().split(' '))
result = [[0] * m2 for _ in range(n1)]
for i in range(n1):
    for j in range(m2):
        for k in range(n2):
            result[i][j] += int(matrix1[i][k]) * int(matrix2[k][j])
for i in range(n1):
    print(*result[i])
