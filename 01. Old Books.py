book = input()

searched_books_counter = 0
searched_books = input()
while searched_books != "No More Books":
    if searched_books == book:
        print(f"You checked {searched_books_counter} books and found it.")
        break
    searched_books_counter += 1
    searched_books = input()
if searched_books == "No More Books":
    print("The book you search is not here!")
    print(f"You checked {searched_books_counter} books.")