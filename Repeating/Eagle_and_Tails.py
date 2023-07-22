s = input()
count = 1
maximum = 1
if 'О' not in s:
    print(len(s))
    exit()
elif 'Р' not in s:
    print(0)
    exit()
for i in range(len(s)):
    if s[i] == s[i - 1] == 'Р':
        count += 1
    else:
        if maximum < count:
            maximum = count
        count = 1
if maximum < count:
    maximum = count
print(maximum)
