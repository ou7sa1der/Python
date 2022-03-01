count_user_names = int(input())

set_users = set()

while count_user_names:
    user = input()
    set_users.add(user)
    count_user_names -= 1

for user in set_users:
    print(user)