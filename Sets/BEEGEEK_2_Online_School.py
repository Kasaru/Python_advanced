m, n = int(input()), int(input())
sn, sm = set(), set()
for i in range(m):
    sm.add(input())
for j in range(n):
    sn.add(input())
print(len(sm - (sn & sm)))