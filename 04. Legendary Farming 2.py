#    • Shadowmourne - requires 250 Shards;
#    • Valanyr - requires 250 Fragments;
#    • Dragonwrath - requires 250 Motes;
def shards_funk(command,element,quantity,key_materials_dict):

    if not element in key_materials_dict:
        key_materials_dict[element] = quantity
    else:
        key_materials_dict[element] += quantity

    return key_materials_dict


def fragments_funk(command,element,quantity,key_materials_dict):

    if not element in key_materials_dict:
        key_materials_dict[element] = quantity
    else:
        key_materials_dict[element] += quantity

    return key_materials_dict


def motes_funk(command, element, quantity, key_materials_dict):
    if not element in key_materials_dict:
        key_materials_dict[element] = quantity
    else:
        key_materials_dict[element] += quantity

    return key_materials_dict


def junk_funk(command,element,quantity,junk_dict):
    if not element in junk_dict:
        junk_dict[element] = quantity
    else:
        junk_dict[element] += quantity

    return junk_dict

#vsichki 3 key elements da se printirat dori da sa 0!
def check_for_all_elements(key_materials_dict):
    if not 'motes' in key_materials_dict:
        key_materials_dict['motes'] = 0
    if not 'fragments' in key_materials_dict:
        key_materials_dict['fragments'] = 0
    if not 'shards' in key_materials_dict:
        key_materials_dict['shards'] = 0
    return key_materials_dict

command = input().split()
key_materials_dict = {}
junk_dict = {}
flag = False

while command != 'stop':
    for material in range(0,len(command),2):
        element = command[material + 1].lower()
        quantity = int(command[material])

        if element == 'shards':
            shards_funk(command,element,quantity,key_materials_dict)
            if key_materials_dict[element] >= 250:
                key_materials_dict[element] -= 250
                print(f'Shadowmourne obtained!')
                flag = True
                break


        elif element == 'fragments':
            fragments_funk(command,element,quantity,key_materials_dict)
            if key_materials_dict[element] >= 250:
                key_materials_dict[element] -= 250
                print(f'Valanyr obtained!')
                flag = True
                break


        elif element == 'motes':
            motes_funk(command,element,quantity,key_materials_dict)
            if key_materials_dict[element] >= 250:
                key_materials_dict[element] -= 250
                print(f'Dragonwrath obtained!')
                flag = True
                break


        else:
            junk_funk(command,element,quantity,junk_dict)



    if flag:
        break
    else:
        command = input().split()


check_for_all_elements(key_materials_dict)

sorted_dict = sorted(key_materials_dict.items(),key=lambda kvp:(-kvp[1],kvp[0]))
sorted_junk = sorted(junk_dict.items(),key=lambda kvp:kvp[0])


for material,value in sorted_dict:
    print(f"{material}: {value}")

for junk,value in sorted_junk:
    print(f"{junk}: {value}")