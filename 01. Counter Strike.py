initial_energy = int(input())

wins = 0

command = input()
while command != "End of battle":
    enemy_distance = int(command)
    if initial_energy - enemy_distance < 0:
        print(f"Not enough energy! Game ends with {wins} won battles and {initial_energy} energy")
        break
    else:
        initial_energy -= enemy_distance
        wins += 1
    if wins % 3 == 0:
        initial_energy += wins
    command = input()
else:
    print(f"Won battles: {wins}. Energy left: {initial_energy}")