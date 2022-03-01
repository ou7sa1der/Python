import math
procesors_count = int(input())
workers_count = int(input())
working_days = int(input())

total_working_hours = workers_count * working_days * 8
work_completed = total_working_hours / 3

if math.floor(work_completed) < procesors_count:
    count_need = procesors_count - math.floor(work_completed)
    loses = count_need * 110.10
    print(f"Losses: -> {loses:.2f} BGN")
else:
    count_left = math.floor(work_completed) - procesors_count
    profit = count_left * 110.10
    print(f"Profit: -> {profit:.2f} BGN")