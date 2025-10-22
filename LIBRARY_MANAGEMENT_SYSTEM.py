# --------------------------------------------
# Library Management System - Demo Script
# --------------------------------------------

# Predefined genres (using a tuple)
GENRES = ("Fiction", "Non-Fiction", "Sci-Fi", "Mystery", "Romance")

# Data structures
books = {}       # Dictionary → ISBN : book details
members = []     # List of dictionaries → member records


# ------------------------------
# Core Functions
# ------------------------------

def add_book(books, isbn, title, author, genre, total_copies, GENRES):
    """Add a new book if ISBN is unique and genre is valid."""
    if isbn in books:
        print(f"Book with ISBN {isbn} already exists.")
        return
    if genre not in GENRES:
        print(f"Invalid genre '{genre}'. Must be one of {GENRES}.")
        return
    books[isbn] = {"title": title, "author": author, "genre": genre, "total_copies": total_copies}
    print(f"Book '{title}' added successfully.")


def add_member(members, member_id, name, email):
    """Add a new member if ID is unique."""
    if any(m["member_id"] == member_id for m in members):
        print(f"Member with ID {member_id} already exists.")
        return
    members.append({"member_id": member_id, "name": name, "email": email, "borrowed_books": []})
    print(f"Member '{name}' added successfully.")


def search_books(books, keyword):
    """Search books by title or author."""
    print(f"\nSearching for '{keyword}'...")
    found = False
    for isbn, details in books.items():
        if keyword.lower() in details["title"].lower() or keyword.lower() in details["author"].lower():
            print(f"{details['title']} by {details['author']} (Genre: {details['genre']}, Copies: {details['total_copies']})")
            found = True
    if not found:
        print("No matching books found.")


def borrow_book(books, members, member_id, isbn):
    """Borrow a book if available and member has not exceeded 3 books."""
    member = next((m for m in members if m["member_id"] == member_id), None)
    if not member:
        print("Member not found.")
        return

    if isbn not in books:
        print("Book not found.")
        return

    if len(member["borrowed_books"]) >= 3:
        print("Member cannot borrow more than 3 books.")
        return

    if books[isbn]["total_copies"] <= 0:
        print("No copies left to borrow.")
        return

    books[isbn]["total_copies"] -= 1
    member["borrowed_books"].append(isbn)
    print(f"'{books[isbn]['title']}' borrowed successfully by {member['name']}.")


def return_book(books, members, member_id, isbn):
    """Return a borrowed book."""
    member = next((m for m in members if m["member_id"] == member_id), None)
    if not member:
        print("Member not found.")
        return

    if isbn not in member["borrowed_books"]:
        print("Member did not borrow this book.")
        return

    member["borrowed_books"].remove(isbn)
    books[isbn]["total_copies"] += 1
    print(f"'{books[isbn]['title']}' returned successfully by {member['name']}.")


def delete_book(books, isbn):
    """Delete a book if it exists and no copies are borrowed."""
    if isbn in books:
        del books[isbn]
        print(f"Book with ISBN {isbn} deleted successfully.")
    else:
        print(f"Book with ISBN {isbn} not found.")


def delete_member(members, member_id):
    """Delete a member if they have no borrowed books."""
    for m in members:
        if m["member_id"] == member_id:
            if m["borrowed_books"]:
                print(f"Cannot delete member {member_id}; books still borrowed.")
                return
            members.remove(m)
            print(f"Member {member_id} deleted successfully.")
            return
    print(f"Member {member_id} not found.")


# ------------------------------
# DEMONSTRATION
# ------------------------------

if __name__ == "__main__":
    print("\n--- Library Management System Demo ---\n")

    # Add some books
    add_book(books, "ISBN001", "The Great Gatsby", "F. Scott Fitzgerald", "Fiction", 3, GENRES)
    add_book(books, "ISBN002", "A Brief History of Time", "Stephen Hawking", "Non-Fiction", 2, GENRES)
    add_book(books, "ISBN003", "Dune", "Frank Herbert", "Sci-Fi", 4, GENRES)

    # Add members
    add_member(members, "M001", "Alice Johnson", "alice@example.com")
    add_member(members, "M002", "Bob Smith", "bob@example.com")

    # Search books
    search_books(books, "dune")

    # Borrow a book
    borrow_book(books, members, "M001", "ISBN003")
    borrow_book(books, members, "M001", "ISBN001")

    # Try borrowing when no copies left
    books["ISBN001"]["total_copies"] = 0
    borrow_book(books, members, "M002", "ISBN001")

    # Return a book
    return_book(books, members, "M001", "ISBN001")

    # Delete operations
    delete_book(books, "ISBN002")
    delete_member(members, "M001")  # Should fail if still borrowed books

    # Show final system state
    print("\n--- Final Library State ---")
    print("Books:", books)
    print("Members:", members)

    print("\nDemo complete.")
