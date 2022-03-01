def converting_dict(whole_string):
    id = str
    students_dict = {}
    while ':' in whole_string:
        split_string = whole_string.split(':')
        name_key = split_string[0]
        id = split_string[1]
        course = split_string[2]
        if id in students_dict:
            return
        students_dict[name_key] = id,course
        whole_string = input()

    whole_string = whole_string.split('_')
    whole_string = ' '.join(whole_string)


    students_list = []
    for key in students_dict:
        if whole_string in students_dict[key]:
            students_list.append(f'{key} - {students_dict[key][0]}')

    for element in students_list:
        print(element)

    return


whole_string = input()
converting_dict(whole_string)
# data = input()
# courses = {}
#
# while ':' in data:
#     student_name,id,course_name = data.split(':')
#     if course_name not in courses:
#         courses[course_name] = {}
#     courses[course_name][id] = student_name
#     data = input()
#
# searched_course = data
# searched_course_as_list = searched_course.split('_')
# searched_course = ' '.join(searched_course_as_list)
#
# for course_name in courses:
#     if course_name == searched_course:
#         for id,name in courses[course_name].items():
#             print(f'{name} - {id}')