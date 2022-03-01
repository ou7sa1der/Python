received_text = input()
vowels_for_remove = ['a', 'o', 'u', 'e', 'i']

final_list = []

for vowel in received_text:
    if vowel.lower() not in vowels_for_remove:
        final_list.append(vowel)

print(''.join(final_list))

# final_list = [vowel for vowel in received_text if vowel.lower() not in vowels_for_remove]
# print(''.join(final_list))
