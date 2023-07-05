s = input()
for i in range(len(s)-1):
  s = s.replace("  "," ")
print(s.count(" ") + 1)