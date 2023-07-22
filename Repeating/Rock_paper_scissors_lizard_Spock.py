timur, ruslan = input(), input()
if timur == "ножницы" and ruslan in ["бумага", "ящерица"] or timur == "бумага" and ruslan in ["камень", "Спок"] \
        or timur == "камень" and ruslan in ["ножницы", "ящерица"] or timur == "ящерица" and ruslan in ["Спок", "бумага"] \
        or timur == "Спок" and ruslan in ["камень", "ножницы"]:
    print("Тимур")
elif ruslan == timur:
    print("ничья")
else:
    print("Руслан")
