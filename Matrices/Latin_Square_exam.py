n = int(input())
matrix = []
chars = [[0] * n for _ in range(n)]
for k in range(n):
    matrix.append(input().split(' '))
for i in range(n):
    for j in range(n):
        chars[i][j] = matrix[j][i]
for i in range(n):
    for j in range(n):
        if matrix[i][j] in chars[i] and chars[i][j] in matrix[i] and str(j + 1) in matrix[i] and str(j + 1) in chars[i]:
            fl = True
        else:
            fl = False
            break
    if not fl:
        break
if fl:
    print("YES")
else:
    print("NO")
