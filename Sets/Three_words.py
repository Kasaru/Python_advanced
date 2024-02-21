a, b, c = input().split()
if sorted(a) == sorted(b) == sorted(c):
    print('YES')
else:
    print('NO')