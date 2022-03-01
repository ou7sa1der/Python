text = input()
list_of_text = list(text)
bomb_power = 0

index = 0

while True:
    if index >= len(list_of_text):
        break
    if list_of_text[index] == '>':
        bomb_power = int(list_of_text[index + 1])
        if bomb_power == 1:
            list_of_text.pop(index + 1)
        else:
            while bomb_power > 0:
                if index + 1 >= len(list_of_text):
                    break
                if list_of_text[index + 1] == '>':
                    bomb_power += int(list_of_text[index + 2])
                    list_of_text.pop(index + 2)
                    index += 1

                else:
                    list_of_text.pop(index + 1)



                bomb_power -= 1
    index += 1

print(''.join(list_of_text))