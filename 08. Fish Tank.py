lenght_cm = int(input())
widht_cm = int(input())
height_cm = int(input())
percent_busy_space = float(input())

aquarium_volume = lenght_cm * widht_cm * height_cm
total_liters = aquarium_volume * 0.001
percent = percent_busy_space * 0.01
liters_needed = total_liters * (1 - percent)

print(liters_needed)