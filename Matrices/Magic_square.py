n = int(input())
matrix = []
check = []
check_sum = []
nd_sum = 0
r_sum = 0
c_sum = 0
for i in range(n):
    matrix.append(input().split(" "))
if n % 2 != 0:
    d_sum = int(matrix[n % 2][n % 2])
else:
    d_sum = 0
for i in range(n):
    for j in range(n):
        if (i == j) or (n - i - 1 == j or n - 1 - j == i and i == j != 0):
            d_sum += int(matrix[i][j])
        r_sum += int(matrix[i][j])
        check.append(matrix[i][j])
for i in range(n):
    for j in range(i, len(check), n):
        c_sum += int(check[j])
    check_sum.append(c_sum)
    if check_sum[i] == check_sum[-i]:
        fl_c = True
    else:
        fl_c = False
        break
    c_sum = 0
for i in range(1, n * n + 1):
    if str(i) in check:
        fl = True
    else:
        fl = False
        break
if (d_sum == r_sum / (n / 2)) and fl and fl_c:
    print('YES')
else:
    print('NO')
