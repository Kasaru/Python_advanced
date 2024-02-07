s, n = input().split(' '), int(input())
l = [[] for i in range(n)]
for i in range(n):
    for j in range(i, len(s), n):
        l[i].append(s[j])
print(l)
