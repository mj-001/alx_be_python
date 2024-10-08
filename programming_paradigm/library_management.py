class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
        self.is_checked_out=False

    def check_out(self):
        if not self.is_checked_out:
            self.is_checked_out=True
        else:
            print(f"'{self.title}' is already checked out.")

    def return_book(self):
        if self.is_checked_out:
            self.is_checked_out=False
        else:
            print(f"'{self.title}' was not checked out.")

    def is_available(self):
        return not self.is_checked_out

    def __str__(self):
        return  f"{self.title} by {self.author}"

class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title==title:
                book.check_out()
                return
        print(f"Book titled '{title}' not found in the library")

    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                book.return_book()
                return
        print(f"Book titled '{title}' not found in the library.")

    def list_available_books(self):
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(book)
        else:
            print(f"No available books in the library.")

