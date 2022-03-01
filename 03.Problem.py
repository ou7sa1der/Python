command = input().split(' ')

chat = []
messages = []
spam = []
while True:
    if 'end' in command:
        break

    if 'Chat' in command:
        message = command[1]
        chat.append(message)

    elif 'Delete' in command:
        message_to_del = command[1]
        if message_to_del in chat:
            chat.remove(message_to_del)

    elif 'Edit' in command:
        message_to_edit = command[1]
        message_edited = command[2]
        if message_to_edit in chat:
            chat.insert(chat.index(message_to_edit), message_edited)
            chat.remove(message_to_edit)

    elif 'Pin' in command:
        message = command[1]
        if message in chat:
            chat.remove(message)
            chat.append(message)

    elif 'Spam' in command:
        command.remove('Spam')
        for messages in command:
            chat.append(messages)

    command = input().split(' ')

for element in chat:
    print(element)