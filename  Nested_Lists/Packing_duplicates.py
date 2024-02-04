def packing(stroka):
    char_list = []
    i = 0
    same = [stroka[i]]
    for i in range(1, len(stroka)):
        if stroka[i] != stroka[i - 1] and i <= len(stroka) - 1:
            char_list.append(same)
            same = []
            same.append(stroka[i])
            if i > len(stroka) - 1:
                char_list.append(same)
        else:
            same.append(stroka[i])
    char_list.append(same)
    print(char_list)


stroka = input().replace(" ", "")
print(stroka)
print(len(stroka))
packing(stroka)
