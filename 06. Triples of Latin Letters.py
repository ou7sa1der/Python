number_of_characters = int(input())

for index_one in range(97, 97 + number_of_characters):
    for index_two in range(97, 97 + number_of_characters):
        for index_three in range(97, 97 + number_of_characters):
            print(chr(index_one)+chr(index_two)+chr(index_three))