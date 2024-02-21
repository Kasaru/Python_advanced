m, n = int(input()), int(input())
sn, sm = set(), set()
for i in range(m):
    sm.add(input())
for j in range(n):
    sn.add(input())
if len((sm | sn) - (sn & sm)) > 0:
    print(len((sm | sn) - (sn & sm)))
else:
    print('NO')