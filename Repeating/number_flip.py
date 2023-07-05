n = int(input())
r = 0
if len(str(n)) == 5:
  while n>0:
    r *= 10
    r += n%10
    n = (n - n%10) //10
else:
  while n > 9:
    r *= 10
    r += n%10
    n = (n - n%10) //10
  r += n*100000
print(r)