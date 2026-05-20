from book import Book
from member import Member
from loan import Loan
from exceptions import (
    BookNotFoundError,
    MemberNotFoundError,
    BookUnavailableError
)

class LibraryService:
    def __init__(self):
        self.books = {}
        self.members = {}
        self.loans = []

    def add_book(self, book):
        self.books[book.book_id] = book

    def add_member(self, member):
        self.members[member.member_id] = member

    def borrow_book(self, book_id, member_id):

        if book_id not in self.books:
            raise BookNotFoundError("Book not found.")

        if member_id not in self.members:
            raise MemberNotFoundError("Member not found.")

        book = self.books[book_id]
        member = self.members[member_id]

        if not book.is_available:
            raise BookUnavailableError("Book unavailable.")

        book.borrow()

        loan = Loan(
            f"L{len(self.loans)+1:03}",
            book,
            member
        )

        self.loans.append(loan)
        return "Book borrowed successfully!"

    def return_book(self, book_id):

        if book_id not in self.books:
            raise BookNotFoundError("Book not found.")

        self.books[book_id].return_book()
        return "Book returned successfully!"

    def display_books(self):
        if not self.books:
            print("No books available.")
            return

        for book in self.books.values():
            book.display_info()
            print()

    def display_members(self):
        if not self.members:
            print("No members available.")
            return

        for member in self.members.values():
            member.display_info()
            print()

    def display_loans(self):
        if not self.loans:
            print("No loans available.")
            return

        for loan in self.loans:
            loan.display()
            print()