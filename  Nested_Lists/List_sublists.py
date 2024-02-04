def sublisting(stroka):
    char_list = [[]]
    for i in range(len(stroka)):
        for j in range(len(stroka)):
            chunk = stroka[j:i + j + 1]
            if len(chunk) == i + 1:
                char_list.append(list(chunk))
                chunk = []
    print(char_list)


stroka = input().replace(" ", "")
sublisting(stroka)
