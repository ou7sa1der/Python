command = input()

phone_book_dict = {}

while not command.isdigit():
    data_split = command.split('-')
    name = data_split[0]
    phone_number = data_split[1]  #ToDo check if int is needed
    phone_book_dict[name] = phone_number
    command = input()

command = int(command)
while command:
    command -= 1
    name = input()
    if name in phone_book_dict:
        print(f"{name} -> {phone_book_dict[name]}")
    else:
        print(f"Contact {name} does not exist.")
