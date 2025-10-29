# operations.py
# Library Management System Functions
# Author: Osman Sheriff

# ---------- Data Structures ----------
books = {}
members = []
genres = ("Fiction", "Non-Fiction", "Sci-Fi", "Education")

# ---------- CRUD + Borrow/Return ----------

def add_book(books, isbn, title, author, genre, total_copies, genres):
    """Add a new book if ISBN is unique and genre is valid."""
    if isbn in books:
        return "Book already exists."
    if genre not in genres:
        return "Invalid genre."
    books[isbn] = {
        "title": title,
        "author": author,
        "genre": genre,
        "total_copies": total_copies,
        "borrowed": 0
    }
    return "Book added successfully."


def search_book(books, title):
    """Search a book by title."""
    for isbn, info in books.items():
        if info["title"].lower() == title.lower():
            return isbn, info
    return None


def update_book(books, isbn, title=None, author=None, total_copies=None):
    """Update book details."""
    if isbn not in books:
        return "Book not found."
    if title:
        books[isbn]["title"] = title
    if author:
        books[isbn]["author"] = author
    if total_copies:
        books[isbn]["total_copies"] = total_copies
    return "Book updated successfully."


def delete_book(books, isbn):
    """Delete a book if it exists."""
    if isbn in books:
        del books[isbn]
        return "Book deleted successfully."
    return "Book not found."


def add_member(members, member_id, name, email):
    """Add a new library member."""
    for m in members:
        if m["member_id"] == member_id:
            return "Member already exists."
    members.append({"member_id": member_id, "name": name, "email": email, "borrowed_books": []})
    return "Member added successfully."


def delete_member(members, member_id):
    """Delete a member only if no borrowed items."""
    for m in members:
        if m["member_id"] == member_id:
            if m["borrowed_books"]:
                return "Member still has borrowed books."
            members.remove(m)
            return "Member deleted successfully."
    return "Member not found."


def borrow_book(books, members, member_id, isbn):
    """Allow a member to borrow a book if available."""
    for m in members:
        if m["member_id"] == member_id:
            if len(m["borrowed_books"]) >= 3:
                return "Member has already borrowed 3 books."
            if isbn not in books:
                return "Book not found."
            book = books[isbn]
            if book["borrowed"] >= book["total_copies"]:
                return "No copies left."
            book["borrowed"] += 1
            m["borrowed_books"].append(isbn)
            return "Book borrowed successfully."
    return "Member not found."


def return_book(books, members, member_id, isbn):
    """Allow a member to return a borrowed book."""
    for m in members:
        if m["member_id"] == member_id:
            if isbn not in m["borrowed_books"]:
                return "This book was not borrowed."
            m["borrowed_books"].remove(isbn)
            books[isbn]["borrowed"] -= 1
            return "Book returned successfully."
    return "Member not found."
