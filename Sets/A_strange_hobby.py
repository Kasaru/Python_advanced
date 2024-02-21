s = set(input().split())
ss = set(input().split())
res = []
if len(ss & s) > 0:
    for i in (ss & s):
        res.append(int(i))
    print(*sorted(res, reverse = True))
else:
    print('BAD DAY')