s = input()
r,k = 0, 0
k = len(s)*60
r = k//100
k -= r*100
print(f"{r} р. {k} коп.")