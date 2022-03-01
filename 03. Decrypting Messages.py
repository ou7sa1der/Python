key = int(input())
number_lines_following = int(input())
password = ''
for letter in range(1, number_lines_following + 1):
    character = input()
    password = (ord(character) + key)
    print(chr(password), end='')
