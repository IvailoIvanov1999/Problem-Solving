favorite_book = input()

books_counter = 0
while True:
    book_names = input()
    books_counter += 1

    if book_names == "No More Books":
        print("The book you search is not here!")
        print(f"You checked {books_counter - 1} books.")
        break
    if favorite_book == book_names:
        print(f"You checked {books_counter - 1} books and found it.")
        break