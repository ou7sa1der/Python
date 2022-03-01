floor = int(input())
count_rooms_on_floor = int(input())

count_floors = 0
count_rooms = 0
counter = 0

for count_floors in range(floor, 0, - 1):
    for count_rooms in range(0, count_rooms_on_floor):
        counter += 1
        if count_floors % 2 == 0 and counter <= count_rooms_on_floor:
            print(f"L{count_floors}{count_rooms}", end=" ")
        elif count_floors % 2 != 0 and counter <= count_rooms_on_floor:
            print(f"L{count_floors}{count_rooms}", end=" ")
        elif count_floors % 2 == 0:
            print(f"O{count_floors}{count_rooms}", end=" ")
        elif count_floors % 2 != 0:
            print(f"A{count_floors}{count_rooms}", end=" ")
    print()