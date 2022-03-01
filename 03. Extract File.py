directory = input().split('\\')


for word in directory:
    if '.' in word:
        last_string = word.split('.')
        file_name = last_string[0]
        extension = last_string[1]
        print(f"File name: {file_name}")
        print(f"File extension: {extension}")