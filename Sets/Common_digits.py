n = int(input())
f = set(input())
ff = []
for i in range(n-1):
    s = set(input())
    f.intersection_update(s)
f = list(f)
for i in range(len(f)):
    ff.append(int(f[i]))
print(*sorted(ff))