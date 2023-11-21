n = int(input())
l = []
for _ in range(n):
    elem = [1 * (k+1) for k in range(n)]
    l.append(elem)
for i in range(len(l)):
    print(l[i])