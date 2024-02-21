n = int(input())
l = []
for i in range(n):
    l.append(input().split(' '))
    print(*l[i])
print()
for i in l:
    if int(i[1]) > 3:
        print(*i)
