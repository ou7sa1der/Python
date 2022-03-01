def synonyms_dict(count_of_the_words:int,word,synonym):
    synonym_dictionary = {}
    count = 0

    while True:
        count += 1
        key = word
        value = synonym

        if key in synonym_dictionary:
            synonym_dictionary[key] += f', {value}'

        else:
            synonym_dictionary[key] = value

        if count >= count_of_the_words:
            break
        else:
            word = input()
            synonym = input()

    return synonym_dictionary

count_of_the_words = int(input())
word = input()
synonym = input()

synonym_dictionary = synonyms_dict(count_of_the_words,word,synonym)

for word in synonym_dictionary:
    print(f'{word} - {synonym_dictionary.get(word)}')