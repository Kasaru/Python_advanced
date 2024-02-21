n = int(input())
m = int(input())
s =set()
for i in range(n):
    s.add(input())
for i in range(m):
    if input() in s:
        print('YES')
    else:
        print('NO')