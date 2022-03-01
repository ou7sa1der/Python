failed_times = int(input())
task_name = input()
grade = int(input())

failed_times_counter = 0
average_grade_counter = 0
tasks_solved_counter = 0
average_grade_sum = 0

while task_name != "Enough":
    if grade <= 4:
        failed_times_counter += 1
        if failed_times_counter == failed_times:
            print(f"You need a break, {failed_times} poor grades.")
            break
    average_grade_counter += 1
    average_grade_sum += grade
    tasks_solved_counter += 1
    last_task_name = task_name
    task_name = input()
    if task_name == "Enough":
        total_average_grade = average_grade_sum / average_grade_counter
        print(f"Average score: {total_average_grade:.2f}")
        print(f"Number of problems: {tasks_solved_counter}")
        print(f"Last problem: {last_task_name}")
        break
    grade = int(input())