hour_of_exam = int(input())
minute_of_exam = int(input())
hour_of_arrival = int(input())
minute_of_arrival = int(input())

#    • "Late", ако студентът пристига по-късно от часа на изпита;
#    • "On time", ако студентът пристига точно в часа на изпита или до 30 минути по-рано;
#    • "Early", ако студентът пристига повече от 30 минути преди часа на изпита.

time_of_exam_min = (hour_of_exam * 60) + minute_of_exam
time_of_arrival_min = (hour_of_arrival * 60) + minute_of_arrival
total_time = 0


if time_of_exam_min == time_of_arrival_min or minute_of_arrival:
