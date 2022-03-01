def string_to_repeat(strings:str,counter:int):
    string_list = []

    for x in range(counter):
        string_list.append(strings)

    return ''.join(map(str,string_list))

string = input()
counter = int(input())

print(string_to_repeat(string,counter))