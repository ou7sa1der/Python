dungeon_rooms = input().split('|')

current_health = 100
bitcoins = 0
room = 0
diff = 0
death_flag = False

for action in dungeon_rooms:
    command = action.split(' ')
    room += 1
    if command[0] == 'potion':
        current_health += int(command[1])
        if current_health > 100:
            diff = int(command[1]) - (current_health - 100)
            current_health = 100
            print(f"You healed for {diff} hp.")
            print(f"Current health: {current_health} hp.")
        else:
            print(f"You healed for {command[1]} hp.")
            print(f"Current health: {current_health} hp.")
        continue
    if command[0] == 'chest':
        print(f"You found {command[1]} bitcoins.")
        bitcoins += int(command[1])
    else:
        current_health -= int(command[1])
        if current_health <= 0:
            print(f"You died! Killed by {command[0]}.")
            death_flag = True
            break
        print(f"You slayed {command[0]}.")

if death_flag:
    print(f"Best room: {room}")
else:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {current_health}")