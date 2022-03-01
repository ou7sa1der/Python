def register_func_unregister_func(type_command):



    split_command = type_command.split(' ')
    if split_command[0] == 'register':
        name = split_command[1]
        license_plate_number = split_command[2]
        if name in registered_dict:
            print(f"ERROR: already registered with plate number {license_plate_number}")
        else:
            print(f"{name} registered {license_plate_number} successfully")
            registered_dict[name] = license_plate_number
    else:
        name = split_command[1]
        if name not in registered_dict:
            print(f"ERROR: user {name} not found")
        else:
            print(f"{name} unregistered successfully")
            del registered_dict[name]


    return registered_dict


number_of_commands = int(input())
registered_dict = {}
for vehicles in range(1,number_of_commands + 1):
    type_command = input()
    registered_dict = register_func_unregister_func(type_command)


for left_users in registered_dict:
    print(f"{left_users} => {registered_dict[left_users]}")