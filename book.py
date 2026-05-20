class Book:
    def __init__(self, book_id, title, author, isbn, year):
        self._book_id = book_id
        self.title = title  # Uses setter
        self._author = author
        self._isbn = isbn
        self._publication_year = year
        self._is_available = True

    # Book ID - Read Only
    @property
    def book_id(self):
        return self._book_id

    # Title Property
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not value or not value.strip():
            raise ValueError("Title cannot be empty!")
        self._title = value.strip()

    # Author Property
    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not value or not value.strip():
            raise ValueError("Author name cannot be empty!")
        self._author = value.strip()

    # Availability
    @property
    def is_available(self):
        return self._is_available

    def mark_as_borrowed(self):
        self._is_available = False

    def mark_as_returned(self):
        self._is_available = True

    def __str__(self):
        status = "Available" if self._is_available else "Borrowed"
        return f"ID: {self._book_id} | Title: {self._title} | Author: {self._author} | Status: {status}"