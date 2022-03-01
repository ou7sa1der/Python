# import string
#
# import char as char
# test_str = "GeeksForGeeKs"
# res = [char for char in test_str if char.isupper()]
# # print("The uppercase characters in string are : " + str(res))
# # # for i in res:
# # #     def convert_list_to_string(res, seperator=''):
# # #         return seperator.join(res)
# # #     full = convert_list_to_string(res)
#
# print(res.index)
#
#
s = input()
def getindices(s):
    return [i for i, c in enumerate(s) if c.isupper()]
print(getindices(s))