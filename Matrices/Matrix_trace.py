n = int(input())
matrix = []
trace = 0
for i in range(n):
    matrix.append(input().split(' '))
    trace += int(matrix[i][i])
print(trace)
