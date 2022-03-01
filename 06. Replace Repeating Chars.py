text = input()

final = ''

for index in range(len(text)):
    if index + 1 >= len(text):
        final += text[index]
        break
    elif text[index] != text[index + 1]:
        final += text[index]


print(final)