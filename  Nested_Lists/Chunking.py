def chunked(stroka, n):
    char_list = []
    chunk = []
    for i in range(0, len(stroka), n):
        if len(stroka) - i >= n:
            for j in range(i, i + n):
                chunk.append(stroka[j])
            char_list.append(chunk)
            chunk = []
        else:
            for j in range(i, len(stroka)):
                chunk.append(stroka[j])
            char_list.append(chunk)
    print(char_list)


stroka, n = input().replace(" ", ""), int(input())
chunked(stroka, n)
