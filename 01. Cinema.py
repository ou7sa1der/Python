project_type = input()
rows = int(input())
columns = int(input())

#    • Premiere – премиерна прожекция, на цена 12.00 лева;
#    • Normal – стандартна прожекция, на цена 7.50 лева;
#    • Discount – прожекция за деца, ученици и студенти на намалена цена от 5.00 лева.

all_seats = rows * columns

if project_type == "Premiere":
    price = all_seats * 12
    print(f"{price:.2f}")
elif project_type == "Normal":
    price = all_seats * 7.50
    print(f"{price:.2f}")
elif project_type == "Discount":
    price = all_seats * 5
    print(f"{price:.2f}")
else:
    print()