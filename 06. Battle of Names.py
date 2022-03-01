def checking_ifs(even_set,odd_set):
    if sum(odd_set) == sum(even_set):
        values_to_print = odd_set.union(even_set)
        return values_to_print
    elif sum(odd_set) > sum(even_set):
        values_to_print = odd_set.difference(even_set)
        return values_to_print
    elif sum(even_set) > sum(odd_set):
        values_to_print = odd_set.symmetric_difference(even_set)
        return values_to_print




count_names = int(input())

sum_char = 0
current_row = 0
odd_set = set()
even_set = set()


while count_names:
    name = ','.join(input())
    splited_name = name.split(',')
    count_names -= 1
    current_row += 1
    for letter in splited_name:
        converted_letter = ord(letter)
        sum_char += converted_letter
    ascii_value = sum_char // current_row
    sum_char = 0
    if ascii_value % 2 == 0:
        even_set.add(ascii_value)
    else:
        odd_set.add(ascii_value)

values_to_print = checking_ifs(even_set, odd_set)
list_to_print = []
for el in values_to_print:
    list_to_print.append(str(el))
final_list = ', '.join(list_to_print)
print(final_list)

