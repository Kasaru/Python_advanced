word = input().lower()
alph = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
s = word + " запретил букву"
i = 0
while len(s.replace(" ", "")) > 0:
    if alph[i] in s:
        s = s + " " + alph[i]
        print(s)
        s = s.replace(alph[i], "").replace("  ", " ").strip()
        i += 1
    else:
        i += 1
