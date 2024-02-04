n, m = int(input()), int(input())
matrix = []
chars = []
for k in range(n):
    matrix.append(input().split(' '))
numbers = input()
i, j = int(numbers[0]), int(numbers[2])
for t in range(n):
    for s in range(m):
        if i == s:
            matrix[t][s], matrix[t][j] = matrix[t][j], matrix[t][s]
    print(*matrix[t])
