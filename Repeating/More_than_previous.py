s = input().split(' ')
c = 0
for i in range(len(s) - 1):
    if int(s[i + 1]) > int(s[i]):
        c += 1
print(c)
