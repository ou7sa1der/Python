character_one = int(input())
character_two = int(input())
searched = ''
for searched_character in range(character_one, character_two + 1):
    searched = chr(searched_character)
    print(searched, end=' ')