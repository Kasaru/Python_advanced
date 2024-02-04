n = int(input())
matrix = []
chars = []
count = 0
for k in range(n):
    matrix.append(input().split(' '))
for i in range(n):
    for j in range(n):
        if matrix[i][j] == matrix[j][i]:
            count += 1
if count == n ** 2:
    print("YES")
else:
    print("NO")
