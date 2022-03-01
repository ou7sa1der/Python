import math
cat_type = input()
gender = input()

if gender == "m":
    if cat_type == "British Shorthair":
        human_months = 13 * 12
        cat_months = human_months / 6
        print(f"{math.floor(cat_months)} cat months")
    elif cat_type == "Siamese":
        human_months = 15 * 12
        cat_months = human_months / 6
        print(f"{math.floor(cat_months)} cat months")
    elif cat_type == "Persian":
        human_months = 14 * 12
        cat_months = human_months / 6
        print(f"{math.floor(cat_months)} cat months")
    elif cat_type == "Ragdoll":
        human_months = 16 * 12
        cat_months = human_months / 6
        print(f"{math.floor(cat_months)} cat months")
    elif cat_type == "American Shorthair":
        human_months = 12 * 12
        cat_months = human_months / 6
        print(f"{math.floor(cat_months)} cat months")
    elif cat_type == "Siberian":
        human_months = 11 * 12
        cat_months = human_months / 6
        print(f"{math.floor(cat_months)} cat months")
    else:
        print(f"{cat_type} is invalid cat!")
elif gender == "f":
    if cat_type == "British Shorthair":
        human_months = 14 * 12
        cat_months = human_months / 6
        print(f"{math.floor(cat_months)} cat months")
    elif cat_type == "Siamese":
        human_months = 16 * 12
        cat_months = human_months / 6
        print(f"{math.floor(cat_months)} cat months")
    elif cat_type == "Persian":
        human_months = 15 * 12
        cat_months = human_months / 6
        print(f"{math.floor(cat_months)} cat months")
    elif cat_type == "Ragdoll":
        human_months = 17 * 12
        cat_months = human_months / 6
        print(f"{math.floor(cat_months)} cat months")
    elif cat_type == "American Shorthair":
        human_months = 13 * 12
        cat_months = human_months / 6
        print(f"{math.floor(cat_months)} cat months")
    elif cat_type == "Siberian":
        human_months = 12 * 12
        cat_months = human_months / 6
        print(f"{math.floor(cat_months)} cat months")
    else:
        print(f"{cat_type} is invalid cat!")