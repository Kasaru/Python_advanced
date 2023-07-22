timur, ruslan = input(), input()
if timur == "ножницы" and ruslan == "бумага" or timur == "бумага" and ruslan == "камень" or timur == "камень" and ruslan == "ножницы":
    print("Руслан")
elif ruslan == timur:
    print("ничья")
else:
    print("Тимур")
