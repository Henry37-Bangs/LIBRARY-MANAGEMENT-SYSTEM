# tests.py
from operations import *

def run_tests():
    # Reset data
    test_books = {}
    test_members = []
    test_genres = ("Fiction", "Non-Fiction")

    # 1. Add book
    result = add_book(test_books, "111", "Python 101", "Osman", "Fiction", 3, test_genres)
    assert result == "Book added successfully."

    # 2. Add duplicate book
    result = add_book(test_books, "111", "Python 101", "Osman", "Fiction", 3, test_genres)
    assert result == "Book already exists."

    # 3. Add member
    result = add_member(test_members, 1, "Selwyn", "selwyn@mail.com")
    assert result == "Member added successfully."

    # 4. Borrow book
    result = borrow_book(test_books, test_members, 1, "111")
    assert result == "Book borrowed successfully."

    # 5. Borrow when no copies left
    test_books["111"]["borrowed"] = 3
    result = borrow_book(test_books, test_members, 1, "111")
    assert result == "No copies left."

    print("All tests passed successfully!")

if __name__ == "__main__":
    run_tests()
