from math import floor
record_in_sec = float(input())
distance_in_m = float(input())
time_in_sec = float(input())

swimming_time_sec = distance_in_m * time_in_sec
delay_time = (floor(distance_in_m / 15)) * 12.5
total_time = swimming_time_sec + delay_time

#Ако НЕ е подобрил рекорда (времето му е по-голямо или равно на рекорда) отпечатваме:
if total_time >= record_in_sec:
    time_needed = total_time - record_in_sec
    print(f'No, he failed! He was {time_needed:.2f} seconds slower.')
#Ако Иван е подобрил Световния рекорд (времето му е по-малко от рекорда) отпечатваме:
else:
    print(f'Yes, he succeeded! The new world record is {total_time:.2f} seconds.')