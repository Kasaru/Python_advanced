n = int(input())
s2 = []
number = []
fl = 0
for i in range(n):
    s = input()
    fl = 0
    for j in range(len(s)):
        if fl == 1:
            break
        if s[j] == 'a':
            s2 += s[j]
            for f in range(j, len(s)):
                if fl == 1:
                    break
                if s[f] == 'n':
                    s2 += s[f]
                    for g in range(f, len(s)):
                        if fl == 1:
                            break
                        if s[g] == 't':
                            s2 += s[g]
                            for h in range(g, len(s)):
                                if fl == 1:
                                    break
                                if s[h] == 'o':
                                    s2 += s[h]
                                    for k in range(h, len(s)):
                                        if s[k] == 'n':
                                            s2 += s[k]
                                            fl = 1
                                            break
            if 'anton' in ''.join(s2):
                number.append(i + 1)
                s2 = []
print(*number)
