given_number = input()
given_number = sorted(given_number, reverse=True)

def convert_list_to_string(org_list, seperator=''):
    """ Convert list to string, by joining all item in list with given separator.
        Returns the concatenated string """
    return seperator.join(org_list)
# Convert list of strings to string
full_str = convert_list_to_string(given_number)
print(full_str)