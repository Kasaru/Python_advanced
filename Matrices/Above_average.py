n = int(input())
matrix = []
count = 0
for i in range(n):
    matrix.append(input().split(' '))
for i in range(n):
    count = 0
    for j in range(n):
        if int(matrix[i][j]) > sum(map(int, matrix[i])) / n:
            count += 1
    print(count)
