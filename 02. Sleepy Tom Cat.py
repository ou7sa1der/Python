from math import floor
rest_days = int(input())

#Ако времето за игра на Том е над нормата за текущата година:
#Ако времето за игра на Том е под нормата за текущата година:
minimum_playing_time = 30000

rest_days_play_time_minutes = 127
work_days_play_time_minutes = 63

work_days = 365 - rest_days
rest_days_minutes = rest_days * rest_days_play_time_minutes
work_days_minutes = work_days * work_days_play_time_minutes
real_play_time = rest_days_minutes + work_days_minutes

if minimum_playing_time > real_play_time:
    time_left = minimum_playing_time - real_play_time
    time_left_hours = time_left / 60
    time_left_minutes = time_left % 60
    print(f'Tom sleeps well')
    print(f'{floor(time_left_hours)} hours and {time_left_minutes} minutes less for play')
else:
    time_left = real_play_time - minimum_playing_time
    time_left_hours = time_left / 60
    time_left_minutes = time_left % 60
    print(f'Tom will run away')
    print(f'{floor(time_left_hours)} hours and {time_left_minutes} minutes more for play')
