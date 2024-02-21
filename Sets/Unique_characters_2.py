n = int(input())
s = ''
for i in range(n):
    s += input().lower()
ss = set(s)
print(len(ss))