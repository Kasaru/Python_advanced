def pascal(n):
    result = []
    for i in range(0, n + 1):
        row = [1] * (i + 1)
        for j in range(i):
            if j != 0 and j != i:
                row[j] = result[i - 1][j - 1] + result[i - 1][j]
        result.append(row)
    return result


n = int(input())
result = pascal(n)
for i in range(n):
    print(*result[i])
