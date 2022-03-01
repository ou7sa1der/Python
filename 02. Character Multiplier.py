two_strings = input().split(' ')
word_one = two_strings[0]
word_two = two_strings[1]

result = 0
i = 0
minimum_lenght = min(len(word_one),len(word_two))
maximum_lenght = max(len(word_one),len(word_two))
last_index = 0
bigger_word = ''

if len(word_one) > len(word_two):
    bigger_word = word_one
else:
    bigger_word = word_two

for index in range(0,minimum_lenght):
    result += ord(word_one[index]) * ord(word_two[index])
    last_index += 1

if maximum_lenght != minimum_lenght:
    for rest_char in range(last_index,maximum_lenght):
        result += ord(bigger_word[rest_char])

print(result)