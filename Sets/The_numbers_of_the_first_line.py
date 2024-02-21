a, b = set(input().split()), set(input().split())
s = list(a - b)
ss = []
for i in range(len(s)):
    ss.append(int(s[i]))
print(*sorted(ss))