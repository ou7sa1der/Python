from math import floor
hours_needed = int(input())
days_got = int(input())
workers_working_over_time = int(input())

hours_worked = (days_got -(days_got * 0.1)) * 8
hours_workers_worked = workers_working_over_time * (2 * days_got)
total_hours = hours_worked + hours_workers_worked

#Ако времето е достатъчно:
if floor(total_hours) >= hours_needed:
    hours_sum = floor(total_hours) - hours_needed
    print(f"Yes!{hours_sum} hours left.")
#Ако  времето НЕ Е достатъчно:
else:
    hours = hours_needed - floor(total_hours)
    print(f"Not enough time!{hours} hours needed.")