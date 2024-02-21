l = input().split()
ss = set()
for i in range(len(l)):
    if int(l[i]) in ss:
        print('YES')
    else:
        print('NO')
        ss.add(int(l[i]))