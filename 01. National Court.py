employee_one = int(input())
employee_two = int(input())
employee_three = int(input())
people_count_in_an_hour = int(input())

hour = 0
total_people = 0
people_answered_for_hour = employee_one + employee_two + employee_three

while people_count_in_an_hour > total_people:
    hour += 1
    if hour % 4 == 0:
        continue
    total_people += people_answered_for_hour
print(f"Time needed: {hour}h.")