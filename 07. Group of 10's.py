received_numbers = list(map(int, input().split(', ')))

the_biggest_number =0

for number in received_numbers:
    if number > the_biggest_number:
        the_biggest_number = number

if the_biggest_number % 10 == 0:
    groups = the_biggest_number / 10
else:
    groups = (the_biggest_number // 10) + 1

while received_numbers:


print(int(groups))
print(list)

# groups = the_biggest_number % 10
# groupz = (the_biggest_number // 10) * 10
#
# for number in received_numbers:
#     if number <= 10 * (number // 10):
#         print(f"Group of {groups * 10}'s: ")
#
# for numbers in groupz:
#     if number <= groupz / 10:
#         print('haa')


#     if number <= 10:
#         list_of_numbers.append(number).
#     if number <= 20:
#         list_of_numbers.append(number)
#     if number <= 30:
#         list_of_numbers.append(number)
#     if number <= 40:
#         list_of_numbers.append(number)
#     if number <= 50:
#         list_of_numbers.append(number)
#
# print(f"Group of {group}'s: {list_of_numbers}")
