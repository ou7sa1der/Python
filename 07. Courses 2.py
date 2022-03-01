def checking_cources(course_name,student_name,dict_to_print):

    if not course_name in dict_to_print:
        dict_to_print[course_name] = [student_name]
    else:
        dict_to_print[course_name] += [f'{student_name}']

    return dict_to_print


command = input()

dict_to_print = {}

while command != 'end':
    command = command.split(' : ')
    course_name = command[0]
    student_name = command[1]

    checking_cources(course_name,student_name,dict_to_print)

    command = input()

dict_count = {}
for name in dict_to_print:
    dict_count[name] = len(dict_to_print[name])


sorted_dict = sorted(dict_count.items(),key=lambda kvp:(-kvp[1],kvp[0]))
sorted_dict_to_print = sorted(dict_to_print.values())

print(dict_to_print)
print(sorted_dict_to_print)
for cource,value in sorted_dict:
    print(f"{cource}: {value}")
    for value in range(len(dict_to_print[cource])):
        print(f'-- {dict_to_print[cource][value]}')