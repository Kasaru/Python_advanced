a, b, c = set(input().split()), set(input().split()), set(input().split())
s = (a | b | c) - (a & b & c)
ss = []
s = list(s)
for i in range(len(s)):
    ss.append(int(s[i]))
print(*sorted(ss))