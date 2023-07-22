s = input().split(' ')
l = []
for i in s:
    if i not in l:
        l.append(i)
print(len(l))