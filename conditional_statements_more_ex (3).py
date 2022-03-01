number = int(input())

if number <= 100:
    bonus_points_numbers = number + 5
    odd_even = number % 2
    if odd_even == 0:
        even = number + 1
        