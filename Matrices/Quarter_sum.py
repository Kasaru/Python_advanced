n = int(input())
matrix = []
up = down = left = right = 0
for i in range(n):
    matrix.append(input().split(' '))
for i in range(n):
    for j in range(n):
        if j < i < n - 1 - j:
            left += int(matrix[i][j])
        elif j > i > n - 1 - j:
            right += int(matrix[i][j])
        elif j < i > n - 1 - j:
            down += int(matrix[i][j])
        elif j > i < n - 1 - j:
            up += int(matrix[i][j])
print(f'Верхняя четверть: {up}\nПравая четверть: {right}\nНижняя четверть: {down}\nЛевая четверть: {left}')
