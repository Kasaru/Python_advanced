s = input().lower()
i = 0
while i < len(s):
    if s[i] in '.,;:-?!':
        s = s.replace(s[i],'')
    i+=1
ss = set(s.split())
print(len(ss))
