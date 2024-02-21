t = {'1','2','3','4','5','6','7','8','9','10','0'}
a, b, c = set(input().split()), set(input().split()), set(input().split())
s = t - (a | b | c)
ss = []
s = list(s)
for i in range(len(s)):
    ss.append(int(s[i]))
print(*sorted(ss))