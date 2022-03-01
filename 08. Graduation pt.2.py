student_name = input()
grades = float(input())

failed_times = 0
average_grade = 0
class_count = 0

while failed_times < 2:
    if grades < 4.00:
        failed_times += 1
        class_count += 1
        if failed_times == 2:
            class_count -= 1
            print(f"{student_name} has been excluded at {class_count} grade")
            break
    elif class_count <= 12:
        average_grade += grades
        class_count += 1
        if class_count == 12:
            total_average_grade = average_grade / 12
            print(f"{student_name} graduated. Average grade: {total_average_grade:.2f}")
            break
    grades = float(input())