f1 = f2 = f3 = 1
n = int(input())
for i in range(n):
    print(f1, end = ' ')
    f1, f2, f3 = f2, f3, f1 + f2 + f3