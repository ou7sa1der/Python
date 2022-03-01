stadium_capacity = int(input())
fans = int(input())

sum_a = 0
sum_b = 0
sum_v = 0
sum_g = 0
all_fans_percent = fans / stadium_capacity * 100

for section in range (1, fans + 1):
    section = input()
    if section == "A":
        sum_a += 1
    elif section == "B":
        sum_b += 1
    elif section == "V":
        sum_v += 1
    elif section == "G":
        sum_g += 1

sum_a_perc = sum_a / fans * 100
sum_b_perc = sum_b / fans * 100
sum_v_perc = sum_v / fans * 100
sum_g_perc = sum_g / fans * 100

print(f"{sum_a_perc:.2f}%")
print(f"{sum_b_perc:.2f}%")
print(f"{sum_v_perc:.2f}%")
print(f"{sum_g_perc:.2f}%")
print(f"{all_fans_percent:.2f}%")