m = int(input())
ss, s, ff = set(), set(), set()
for i in range(m):
    n = int(input())
    ss.clear()
    for j in range(n):
        ss.add(input())
    if m > 1 >= i:
        s = set(s)
        ff = ss & s
        s = list(ss)
    elif m > 1 < i:
        s = set(s)
        ff = ss & s & ff
        s = list(ss)
    else:
        ff = ss
print(*sorted(ff), sep = '\n')