tabs_opened_in_browser = int(input())
wage = int(input())

wage_left = 0
fine_count = 0

for tabs_opened_in_browser in range(1, tabs_opened_in_browser + 1):
    site_name = input()
    if site_name == "Facebook" and tabs_opened_in_browser <= 1:
        fine_count += 1
        wage_left = wage - 150
        if wage_left <= 0:
            print("You have lost your salary.")
            break
    elif site_name == "Facebook":
        fine_count += 1
        wage_left -= 150
        if wage_left <= 0:
            print("You have lost your salary.")
            break
    if site_name == "Instagram" and tabs_opened_in_browser <= 1:
        fine_count += 1
        wage_left = wage - 100
        if wage_left <= 0:
            print("You have lost your salary.")
            break
    elif site_name == "Instagram":
        fine_count += 1
        wage_left -= 100
        if wage_left <= 0:
            print("You have lost your salary.")
            break
    if site_name == "Reddit" and tabs_opened_in_browser <= 1:
        fine_count += 1
        wage_left = wage - 50
        if wage_left <= 0:
            print("You have lost your salary.")
            break
    elif site_name == "Reddit":
        fine_count += 1
        wage_left -= 50
        if wage_left <= 0:
            print("You have lost your salary.")
            break

if fine_count > 0 and wage_left > 0:
    print(wage_left)
elif fine_count <= 0 and wage_left <= 0:
    print(wage)
else:
    print()