employees_list = list(map(int, input().split(' ')))
happines_factor = int(input())

multiplyied_happines_list = [multiplyied_happines * happines_factor for multiplyied_happines in employees_list]
average_happines = sum(multiplyied_happines_list) / len(employees_list)
happy_count_list = [happy_person for happy_person in multiplyied_happines_list if happy_person >= average_happines]
happy_employees_number = len(happy_count_list)
if happy_employees_number >= len(employees_list) / 2:
    print(f"Score: {happy_employees_number}/{len(employees_list)}. Employees are happy!")
else:
    print(f"Score: {happy_employees_number}/{len(employees_list)}. Employees are not happy!")