length = int(input())
l = []
fl = 0
for i in range(length):
    l.append(int(input()))
num = int(input())
for i in range(length):
    for j in range(i+1, length):
        if num == l[i] * l[j]:
            fl = 1
if fl == 1:
    print("ДА")
else:
    print("НЕТ")
