from math import floor
time_one = int(input())
time_two = int(input())
time_three = int(input())

time_sum = time_one + time_two + time_three

minutes = time_sum / 60
seconds = time_sum % 60

minutes = floor(minutes)

if seconds < 10:
    print(f'{minutes}:0{seconds}')
else:
    print(f'{minutes}:{seconds}')