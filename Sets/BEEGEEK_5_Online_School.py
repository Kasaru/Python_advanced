m, n = int(input()), int(input())
sm = []
for i in range(m+n):
    sm.append(input())
sn = set(sm)
if (len(sn) - (len(sm) - len(sn))) > 0:
    print(len(sn) - (len(sm) - len(sn)))
else:
    print('NO')