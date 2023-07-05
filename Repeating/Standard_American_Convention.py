n = input()
l = list(n)
s = ""
for i in range(len(l)-3,0,-3):
  l.insert(i, ",")
print(s.join(l))