students = int(input())

top_students_count = 0
between_four_and_four_point_nine = 0
between_three_and_three_point_nine = 0
fail_under_three = 0
average_sum = 0

for grade in range(1, students + 1):
    grade = float(input())
    if grade < 3:
        fail_under_three += 1
    elif grade >= 3 and grade <= 3.99:
        between_three_and_three_point_nine += 1
    elif grade >= 4 and grade <= 4.99:
        between_four_and_four_point_nine += 1
    elif grade >= 5:
        top_students_count += 1
    average_sum += grade


top_students_perc = top_students_count / students * 100
between_four_and_four_point_nine_perc = between_four_and_four_point_nine / students * 100
between_three_and_three_point_nine_perc = between_three_and_three_point_nine / students * 100
fail_under_three_perc = fail_under_three / students * 100
total_average = average_sum / students
print(f"Top students: {top_students_perc:.2f}%")
print(f"Between 4.00 and 4.99: {between_four_and_four_point_nine_perc:.2f}%")
print(f"Between 3.00 and 3.99: {between_three_and_three_point_nine_perc:.2f}%")
print(f"Fail: {fail_under_three_perc:.2f}%")
print(f"Average: {total_average:.2f}")