import codecs
letters = ['а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р', 'с', 'т', 'у','ф','х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
file = codecs.open('input.txt', 'r', "utf_8_sig")
b = [line if line[1].isalpha() else line.split() for line in file]
file.close()
wfile = open("output.txt", "w")
for j in b:
    print()
    wfile.write('\n')
    for i in j:
        if i.isdigit():
            print(letters[int(i)-1], end='')
            wfile.write(f'{letters[int(i)-1]}')
        elif i.isalpha():
            print(letters[letters.index(i.lower()) - 1], end='')
            wfile.write(f'{letters[letters.index(i.lower()) - 1]}')
wfile.close()
