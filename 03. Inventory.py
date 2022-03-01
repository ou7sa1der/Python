list_of_inventory = input().split(', ')

collected_items = list_of_inventory

command = input().split(' - ')
while not 'Craft!' in command:
    if 'Collect' in command:
        if command[1] in collected_items:
            continue
        else:
            collected_items.append(command[1])
    elif 'Drop' in command:
        if command[1] in collected_items:
            collected_items.remove(command[1])
    elif 'Combine Items' in command:
        new_items = command[1].split(':')
        if new_items[0] in collected_items:
            index = collected_items.index(new_items[0])
            collected_items.insert(index + 1,new_items[1])
    elif 'Renew' in command:
        if command[1] in collected_items:
            collected_items.remove(command[1])
            collected_items.append(command[1])
    command = input().split(' - ')
print(', '.join(map(str,collected_items)))


# def check_item_exist(check_item, all_items):
#     all_items = set(all_items)
#     if check_item in all_items:
#         return True
#     else:
#         return False
#
#
# items = input().split(", ")
#
# command = input()
#
# while not command == "Craft!":
#     type_command = command.split(" - ")[0]
#     item = command.split(" - ")[1]
#     is_exist = check_item_exist(item, items)
#     if type_command == "Collect" and not is_exist:
#         items.append(item)
#     elif type_command == "Drop" and is_exist:
#         items.remove(item)
#     elif type_command == "Combine Items":
#         old_item = item.split(":")[0]
#         new_item = item.split(":")[1]
#         is_exist = check_item_exist(old_item, items)
#         if is_exist:
#             index = items.index(old_item)
#             items.insert(index + 1, new_item)
#     elif type_command == "Renew" and is_exist:
#         index = items.index(item)
#         x = items.pop(index)
#         items.append(x)
#     command = input()
#
# print(", ".join(items))