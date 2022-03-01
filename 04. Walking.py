steps = input()

going_home_steps = 0
steps_sum = 0

while steps != "Going home":
    steps_sum += int(steps)
    if steps_sum >= 10000:
        difference = steps_sum - 10000
        print("Goal reached! Good job!")
        print(f"{difference} steps over the goal!")
        break
    steps = input()
if steps_sum < 10000 and steps != "Going home":
    difference = 10000 - steps_sum
    print(f"{difference} more steps to reach goal.")

if steps == "Going home":
    steps_to_home = int(input())
    going_home_steps = steps_sum + steps_to_home
    if going_home_steps >= 10000:
        difference = going_home_steps - 10000
        print("Goal reached! Good job!")
        print(f"{difference} steps over the goal!")
    elif going_home_steps < 10000:
        difference = 10000 - going_home_steps
        print(f"{difference} more steps to reach goal.")