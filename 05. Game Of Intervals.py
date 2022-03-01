moves_in_the_game = int(input())

numbers = 0
zero_to_nine_count = 0
ten_to_nineteen_count = 0
twenty_to_twentynine_count = 0
thirty_to_thirtynine_count = 0
forty_to_fifty_count = 0
invalid_count = 0
points_sum = 0

for numbers in range(1, moves_in_the_game + 1):
    numbers = int(input())
    zero_to_nine = numbers * 0.20
    ten_to_nineteen = numbers * 0.30
    twenty_to_twentynine = numbers * 0.40
    thirty_to_thirtynine = 50
    forty_to_fifty = 100
    if numbers >= 0 and numbers <= 50:
        if numbers < 10:
            points_sum += zero_to_nine
            zero_to_nine_count += 1
        elif numbers < 20:
            points_sum += ten_to_nineteen
            ten_to_nineteen_count += 1
        elif numbers < 30:
            points_sum += twenty_to_twentynine
            twenty_to_twentynine_count += 1
        elif numbers < 40:
            points_sum += 50
            thirty_to_thirtynine_count += 1
        else:
            points_sum += 100
            forty_to_fifty_count += 1
    else:
        points_sum /= 2
        invalid_count += 1

zero_to_nine_perc = zero_to_nine_count / moves_in_the_game * 100
ten_to_nineteen_perc = ten_to_nineteen_count / moves_in_the_game * 100
twenty_to_twentynine_perc = twenty_to_twentynine_count / moves_in_the_game * 100
thirty_to_thirtynine_perc = thirty_to_thirtynine_count / moves_in_the_game * 100
forty_to_fifty_perc = forty_to_fifty_count / moves_in_the_game * 100
invalid_perc = invalid_count / moves_in_the_game * 100
print(f"{points_sum:.2f}")
print(f"From 0 to 9: {zero_to_nine_perc:.2f}%")
print(f"From 10 to 19: {ten_to_nineteen_perc:.2f}%")
print(f"From 20 to 29: {twenty_to_twentynine_perc:.2f}%")
print(f"From 30 to 39: {thirty_to_thirtynine_perc:.2f}%")
print(f"From 40 to 50: {forty_to_fifty_perc:.2f}%")
print(f"Invalid numbers: {invalid_perc:.2f}%")