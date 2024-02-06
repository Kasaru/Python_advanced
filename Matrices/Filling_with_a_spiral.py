def go_up(n, m, num, count, circle):
    if num < n * m:
        for i in range(count - (circle * 2), n + 1):
            for j in range(circle, circle + 1):
                if num < n * m:
                    num += 1
                    matrix[n - i + 1 + circle][j] = str(num).ljust(3)
        count += 1
        circle += 1
        go_right(n, m, num, count, circle)


def go_down(n, m, num, count, circle):
    if num < n * m:
        if circle >= 3:
            cc = circle + 1
        else:
            cc = count // (circle + 1)
        for i in range(cc, n - circle):
            for j in range(m - (circle + 1), m - circle):
                if num < n * m:
                    num += 1
                    matrix[i][j] = str(num).ljust(3)
        count += 1
        go_left(n, m, num, count, circle)


def go_left(n, m, num, count, circle):
    if num < n * m:
        for i in range(n - (circle + 1), n - circle):
            for j in range(circle + 1, m - circle):
                if num < n * m:
                    num += 1
                    matrix[i][m - j - 1] = str(num).ljust(3)
        count += 1
        go_up(n, m, num, count, circle)


def go_right(n, m, num, count, circle):
    if num < n * m:
        for j in range(circle, m - circle):
            if num < n * m:
                num += 1
                matrix[circle][j] = str(num).ljust(3)
    count += 1
    go_down(n, m, num, count, circle)


n, m = input().split(' ')
n, m = int(n), int(m)
matrix = [['0'.ljust(3)] * m for _ in range(n)]
num = 0
count = 0
circle = 0
go_right(n, m, num, count, circle)
for i in range(n):
    print(*matrix[i])
