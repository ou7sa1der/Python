def checking_courses(command):

    courses_dictonary = {}
    while command != 'end':
        spliting_command = command.split(' : ')
        course_name = spliting_command[0]
        student_name = spliting_command[1]
        if course_name in courses_dictonary:
            courses_dictonary[course_name] += [student_name]
        else:
            courses_dictonary[course_name] = [student_name]

        command = input()

    #for k in sorted(d, key=lambda k: len(d[k]), reverse=True):
    for key in sorted(courses_dictonary,key= lambda k: len(courses_dictonary[k]), reverse=True):  #sortira mi go po goleminata na duljinata na lista v rechnika
        print(f'{key}: {len(courses_dictonary[key])}')
        for name in sorted(courses_dictonary[key]): #sortira mi gi po imenata v lista
            print(f'-- {name}')


command = input()

checking_courses(command)