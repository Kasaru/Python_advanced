n = int(input())
a = []
for i in range(n):
    a.append(input().split(" "))
for i in range(n):
    for j in range(n):
        print(a[n-j-1][i], end=' ')
    print()
