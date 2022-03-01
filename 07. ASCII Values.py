list_of_characters = input().split(', ')

ascii_dict = {}

for character in list_of_characters:
    key = character
    value = ord(character)
    ascii_dict[key] = value

print(ascii_dict)