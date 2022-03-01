import math
number_of_persons = int(input())
total_kg = int(input())

courses = number_of_persons / total_kg
print(math.ceil(courses))
