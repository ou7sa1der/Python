string_received = input().split(' ')

even_lenght_words = [word for word in string_received if len(word) % 2 == 0]
for words in even_lenght_words:
    print(words)