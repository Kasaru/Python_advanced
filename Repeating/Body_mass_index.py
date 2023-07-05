m = float(input())
h = float(input())
if 18.5<=m/h**2<=25:
  print("Оптимальная масса")
elif m/h**2>25:
  print("Избыточная масса")
else:
  print("Недостаточная масса")