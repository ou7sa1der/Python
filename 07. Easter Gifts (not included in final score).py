received_gifts = input().split(' ')
command = input()
received_gifts = list(received_gifts)
new_list = list(received_gifts)
while command != 'No Money':
    command = command.split()
    if 'OutOfStock' in command:
        new_list = i.replace(command[1],'None') for i in new_list
        # new_list = []
        # for i in received_gifts:
        #     new_gift = str.replace(i, command[1], 'None', -1)
        #     new_list.append(new_gift)
    elif 'Required' in command and len(received_gifts) > int(command[2]):
        replacing_index = int(command[2])
        new_list[replacing_index] = command[1]
    elif 'JustInCase' in command:
        new_list[-1] = command[1]
    received_gifts = list(new_list)
    command = input()

while 'None' in received_gifts:
    received_gifts.remove('None')
for i in received_gifts:
    print(i, end=' ')