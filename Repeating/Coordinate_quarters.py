count = int(input())
ft, s, t, fr = 0, 0, 0, 0
for i in range(count):
    coordinates = input().split(' ')
    x = int(coordinates[0])
    y = int(coordinates[1])
    if x > 0 and y > 0:
        ft += 1
    elif x < 0 and y > 0:
        s += 1
    elif x < 0 and y < 0:
        t += 1
    elif x > 0 and y < 0:
        fr += 1
print(f"Первая четверть: {ft} \nВторая четверть: {s} \nТретья четверть: {t} \nЧетвертая четверть: {fr}")
