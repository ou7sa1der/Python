jury_count = int(input())
presentation_name = input()

sum_grades = 0
sum_average_grades = 0
presentation_count = 0

while True:
    if presentation_name == "Finish":
        break
    presentation_count += 1
    sum_grades = 0
    for i in range(1, jury_count + 1):
        grade = float(input())
        sum_grades += grade
    average_grade = sum_grades / jury_count
    sum_average_grades += average_grade
    print(f"{presentation_name} - {average_grade:.2f}.")
    presentation_name = input()
total_sum_average_grades = sum_average_grades / presentation_count
print(f"Student's final assessment is {total_sum_average_grades:.2f}.")