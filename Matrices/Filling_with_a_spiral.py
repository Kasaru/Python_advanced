def go_up(n,m, num,count,circle):
    if num <= n*m:
        for i in range(count - circle,n):
            for j in range(1):
                num += 1
                matrix[n-i+1][j] = str(num).ljust(3)
        for i in range(n):
            print(*matrix[i])
        print()
        count += 1
        circle += 1
        go_right(n,m, num,count,circle)

def go_down(n,m, num,count,circle):
    if num <= n * m:
        for i in range(count - circle,n):
            for j in range(m-1,m):
                num += 1
                matrix[i][j] = str(num).ljust(3)
        for i in range(n):
            print(*matrix[i])
        print()
        count += 1
        go_left(n,m, num,count,circle)

def go_left(n,m, num,count,circle):
    if num <= n * m:
        for i in range(n-1,n):
            for j in range(count - 1 - circle,m):
                num += 1
                matrix[i][m - j - 1] = str(num).ljust(3)
        for i in range(n):
            print(*matrix[i])
        print()
        count += 1
        go_up(n,m, num,count,circle)

def go_right(n,m, num,count,circle):
    if num <= n * m:
        for j in range(count-circle,m):
            num += 1
            matrix[circle][j] = str(num).ljust(3)
    for i in range(n):
        print(*matrix[i])
    print()
    count += 1
    go_down(n,m, num,count,circle)

n, m = input().split(' ')
n, m = int(n), int(m)
matrix = [['0'.ljust(3)] * m for _ in range(n)]
num = 0
count = 0
circle = 0
go_right(n,m,num,count,circle)
# for i in range(n):
#     print(*matrix[i])