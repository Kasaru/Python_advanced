n, m = int(input()), int(input())
matrix = []
row = []
for i in range(n):
    for j in range(m):
        row.append(str(i * j).ljust(3))
    matrix.append(row)
    row = []
for i in range(n):
    print(*matrix[i], end='\n')
