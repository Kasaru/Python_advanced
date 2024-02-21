a, b, c = set(input().split()), set(input().split()), set(input().split())
s = list((a & b) - c)
ss = []
for i in range(len(s)):
    ss.append(int(s[i]))
print(*sorted(ss, reverse = True))