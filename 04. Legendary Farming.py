# • Shadowmourne - requires 250 Shards;
# • Valanyr - requires 250 Fragments;
# • Dragonwrath - requires 250 Motes;
def turning_to_dict(elements_received):
    elements_received = elements_received.split(' ')
    elements_received_dict = {}

    for element_key in range(len(elements_received)):
        element_key = 0
        key = elements_received[element_key + 1]
        value = elements_received[element_key]
        if key in elements_received_dict:
            elements_received_dict[key] = int(elements_received_dict[key]) + int(value)
            elements_received_dict[key] = str(elements_received_dict[key])
            if int(elements_received_dict[key]) >= 250:
                return elements_received_dict
        else:
            elements_received_dict[key] = value
            elements_received_dict[key] = str(elements_received_dict[key])
            if int(elements_received_dict[key]) >= 250:
                return elements_received_dict
        elements_received.remove(key)
        elements_received.remove(value)
        if elements_received == []:
            return elements_received_dict


def adding_additional_input_to_dict(elements_received,elements_received_dict):

    elements_received = turning_to_dict(elements_received)
    new_elements_dict = elements_received

    for key in new_elements_dict:
        if key in elements_received_dict:
            elements_received_dict[key] = int(elements_received_dict[key]) + int(new_elements_dict[key])
            elements_received_dict[key] = str(elements_received_dict[key])
            if int(elements_received_dict[key]) >= 250:
                return elements_received_dict
        else:
             elements_received_dict[key] = new_elements_dict[key]
             if int(elements_received_dict[key]) >= 250:
                return elements_received_dict
    return elements_received_dict


def sorting_print_list_one(elements_received_dict):
    # • On the next three lines, print the remaining key materials in descending order by quantity
    #     ◦ If two key materials have the same quantity, print them in alphabetical order
    dict_for_print = {}
    #flag = False
    junk_dict = {}
    for key,value in elements_received_dict.items():
        # if value in dict_for_print.values():
        #     flag = True

        if key == 'fragments':
            dict_for_print[key] = value
        elif key == 'shards':
            dict_for_print[key] = value
        elif key == 'motes':
            dict_for_print[key] = value
        else:
            junk_dict[key] = value

    if 'fragments' or 'shards' or 'motes' not in dict_for_print:
        value = 0
        if 'fragments' not in dict_for_print:
            key = 'fragments'
            dict_for_print[key] = value
        elif 'shards' not in dict_for_print:
            key = 'shards'
            dict_for_print[key] = value
        elif 'motes' not in dict_for_print:
            key = 'motes'
            dict_for_print[key] = value

    for key, value in dict_for_print.items():
        dict_for_print[key] = int(value)
    for key, value in junk_dict.items():
        junk_dict[key] = int(value)

    #if flag:
    junk_dict = {val[0]: val[1] for val in sorted(junk_dict.items(), key=lambda x: (x[0]))}
    dict_for_print = {val[0]: val[1] for val in sorted(dict_for_print.items(), key=lambda x: (-x[1], x[0]))}
    for key, value in dict_for_print.items():
        print(f'{key}: {dict_for_print[key]}')

    for key, value in junk_dict.items():
        print(f'{key}: {junk_dict[key]}')
    # else:
    #     for key,value in sorted(dict_for_print.items(),key=lambda x: ((x[1]),x[0]), reverse=True):
    #         print(f'{key}: {value}')



    # dict_for_print = {val[0]: val[1] for val in sorted(dict_for_print.items(), key=lambda x: (-x[1], x[0]))}

    return


elements_received = input().lower()
elements_received_dict = turning_to_dict(elements_received)
object_obtained = False

while True:
    for key in elements_received_dict:
        if int(elements_received_dict[key]) >= 250 and key == 'motes':
            print('Dragonwrath obtained!')
            object_obtained = True
            elements_received_dict[key] = int(elements_received_dict[key]) - 250
            elements_received_dict[key] = str(elements_received_dict[key])
            break
        elif int(elements_received_dict[key]) >= 250 and key == 'shards':
            print('Shadowmourne obtained!')
            object_obtained = True
            elements_received_dict[key] = int(elements_received_dict[key]) - 250
            elements_received_dict[key] = str(elements_received_dict[key])
            break
        elif int(elements_received_dict[key]) >= 250 and key == 'fragments':
            print('Valanyr obtained!')
            object_obtained = True
            elements_received_dict[key] = int(elements_received_dict[key]) - 250
            elements_received_dict[key] = str(elements_received_dict[key])
            break

    if object_obtained:
        break
    else:
        elements_received = input().lower()

    adding_additional_input_to_dict(elements_received, elements_received_dict)

sorting_print_list_one(elements_received_dict)


# • On the final several lines, print the junk items in alphabetical order
#     ◦ All materials are printed in format {material}: {quantity}
#     ◦ The output should be lowercase, except for the first letter of the legendary
