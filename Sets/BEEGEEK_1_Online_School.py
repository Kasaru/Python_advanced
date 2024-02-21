ask,answ = set(input().split()), set(input().split())
if ask.issuperset(answ) and len(ask) == len(answ):
    print('YES')
else:
    print('NO')