def charlist(begin, end):
    charlist = []
    first_str = ord(begin)
    second_str = ord(end)
    for i in range(first_str, second_str + 1):
        if i == first_str or i == second_str:
            continue
        else:
            charlist.append(chr(i))
    return ' '.join(charlist)

character_one = input()
character_two = input()

print(charlist(character_one,character_two))