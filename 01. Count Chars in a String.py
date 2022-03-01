# received_string = input().split(' ')
#
# characters_list = ''.join(received_string)
#
# empty_list = []
#
# for character in characters_list:
#     empty_list.append(character)
#
#
#
#
# print(empty_list)


def char_frequency(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        elif n == ' ':
            continue
        else:
            dict[n] = 1
    return dict
received_string = input()
dict = char_frequency(received_string)

for char in dict:

    print(f'{char} -> {dict[char]}')