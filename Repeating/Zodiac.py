y = int(input())
l = ["Дракон", "Змея", "Лошадь", "Овца", "Обезьяна",  "Петух", "Собака", "Свинья", "Крыса", "Бык", "Тигр", "Заяц"]
print(l[(2000-y)%12*-1])