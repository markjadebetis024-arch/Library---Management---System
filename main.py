from book import Book
from member import Member
from loan import Loan

class LibrarySystem:
    def __init__(self):
        self.books = []
        self.members = []
        self.loans = []

    def add_book(self, book):
        self.books.append(book)
        print(f"\u2705 Book '{book.title}' added successfully!")

    def add_member(self, member):
        self.members.append(member)
        print(f"\u2705 Member '{member.name}' added successfully!")

    def borrow_book(self, loan_id, book_id, member_id):
        book = next((b for b in self.books if b.book_id == book_id), None)
        member = next((m for m in self.members if m.member_id == member_id), None)

        if not book:
            print("\u274C Book not found!")
            return
        if not member:
            print("\u274C Member not found!")
            return
        if not book.is_available:
            print("\u274C Book is already borrowed!")
            return

        new_loan = Loan(loan_id, book, member, date.today())
        book.mark_as_borrowed()
        self.loans.append(new_loan)
        print(f"\u2705 Loan created! '{book.title}' borrowed by {member.name}.")

    def return_book(self, loan_id):
        loan = next((l for l in self.loans if l._loan_id == loan_id), None)
        if not loan:
            print("\u274C Loan record not found!")
            return
        if not loan.is_active:
            print("\u274C This book has already been returned!")
            return

        loan.complete_return(date.today())
        print(f"\u2705 Book '{loan._book.title}' returned successfully!")

    def display_books(self):
        print("\n\U0001F4DA LIST OF BOOKS \U0001F4DA")
        if not self.books:
            print("No books in the library.")
        for book in self.books:
            print(book)

    def display_members(self):
        print("\n\U0001F465 LIST OF MEMBERS \U0001F465")
        if not self.members:
            print("No members registered.")
        for member in self.members:
            print(member)

    def display_loans(self):
        print("\n\U0001F4D6 LOAN RECORDS \U0001F4D6")
        if not self.loans:
            print("No loan transactions.")
        for loan in self.loans:
            print(loan)


# --------------------------
# MAIN MENU
# --------------------------
def main():
    library = LibrarySystem()

    while True:
        print("\n" + "="*35)
        print("      LIBRARY MANAGEMENT SYSTEM")
        print("="*35)
        print("1. Add New Book")
        print("2. Add New Member")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. View All Books")
        print("6. View All Members")
        print("7. View All Loans")
        print("8. Exit")
        print("-"*35)

        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            try:
                bid = input("Enter Book ID: ")
                title = input("Enter Title: ")
                author = input("Enter Author: ")
                isbn = input("Enter ISBN: ")
                year = input("Enter Publication Year: ")
                new_book = Book(bid, title, author, isbn, year)
                library.add_book(new_book)
            except ValueError as e:
                print(f"\u274C Error: {e}")

        elif choice == "2":
            try:
                mid = input("Enter Member ID: ")
                name = input("Enter Full Name: ")
                email = input("Enter Email: ")
                phone = input("Enter Phone Number: ")
                new_member = Member(mid, name, email, phone)
                library.add_member(new_member)
            except ValueError as e:
                print(f"\u274C Error: {e}")

        elif choice == "3":
            lid = input("Enter Loan ID: ")
            bid = input("Enter Book ID to borrow: ")
            mid = input("Enter Member ID: ")
            library.borrow_book(lid, bid, mid)

        elif choice == "4":
            lid = input("Enter Loan ID to return: ")
            library.return_book(lid)

        elif choice == "5":
            library.display_books()

        elif choice == "6":
            library.display_members()

        elif choice == "7":
            library.display_loans()

        elif choice == "8":
            print("\U0001F44B Thank you for using Library System! Goodbye!")
            break

        else:
            print("\u274C Invalid choice! Please enter a number between 1-8.")


if _name_ == "_main_":
    main()
