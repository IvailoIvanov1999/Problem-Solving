class Book:
    def __init__(self, book_name: str, author: str, pages: int):
        self.name = book_name
        self.author = author
        self.pages = pages


book = Book("My Book", "Me", 200)
print(book.name)
print(book.author)
print(book.pages)
