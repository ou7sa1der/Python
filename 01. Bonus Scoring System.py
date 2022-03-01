count_of_students = int(input())
count_of_lectures = int(input())
initial_bonus = int(input())

the_biggest_bonus = 0
max_attendances = 0

for student in range(1, count_of_students + 1):
    attendances_for_student = int(input())
    total_bonus = attendances_for_student / count_of_lectures * (5 + initial_bonus)
    if total_bonus >= the_biggest_bonus:
        the_biggest_bonus = total_bonus
        max_attendances = attendances_for_student

print(f"Max Bonus: {round(the_biggest_bonus)}.")
print(f"The student has attended {max_attendances} lectures.")