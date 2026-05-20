from book import Book
from member import Member

class Loan:
    def __init__(self, loan_id, book, member, borrow_date):
        self._loan_id = loan_id
        self._book = book  # Stores Book object
        self._member = member  # Stores Member object
        self._borrow_date = borrow_date
        self._return_date = None

    # Check if loan is still active
    @property
    def is_active(self):
        return self._return_date is None

    # Complete the return
    def complete_return(self, return_date):
        self._return_date = return_date
        self._book.mark_as_returned()  # Update book status

    def __str__(self):
        status = "Active" if self.is_active else f"Returned on {self._return_date}"
        return f"Loan ID: {self._loan_id} | Book: '{self._book.title}' | Borrower: {self._member.name} | Status: {status}"