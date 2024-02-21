n = int(input())
s = set()
for i in range(n):
    s.add(input())
if input() in s:
    print('REPEAT')
else:
    print('OK')