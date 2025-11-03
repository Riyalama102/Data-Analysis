# LMS => Library Management System (Using File Handling)
# Features:
# 1. Add books
# 2. Update books
# 3. Remove books
# 4. View books
# 5. Exit

import os

class LMS:
    filename = "books.txt"

    def __init__(self):
        # Create the file if it doesn't exist
        if not os.path.exists(self.filename):
            file = open(self.filename, "w")
            file.close()

    # Load all books from file
    def load_books(self):
        file = open(self.filename, "r")
        books = []
        for line in file:
            books.append(line.strip())
        file.close()
        return books

    # Save all books to file
    def save_books(self, books):
        file = open(self.filename, "w")
        for book in books:
            file.write(book + "\n")
        file.close()

    # Add a new book
    def add_book(self, name, author, pages):
        file = open(self.filename, "a")
        file.write(f"{name} | {author} | {pages}\n")
        file.close()
        print(f"'{name}' added successfully.")

    # Update book name
    def update_book(self, old_name, new_name):
        books = self.load_books()
        updated = False

        for i in range(len(books)):
            if books[i].startswith(old_name + " |"):
                parts = books[i].split(" | ")
                books[i] = f"{new_name} | {parts[1]} | {parts[2]}"
                updated = True
                break

        if updated:
            self.save_books(books)
            print(f"'{old_name}' updated to '{new_name}'.")
        else:
            print(" Book not found!")

    # Remove a book
    def remove_book(self, name):
        books = self.load_books()
        new_books = []
        removed = False

        for book in books:
            if book.startswith(name + " |"):
                removed = True
                continue
            new_books.append(book)

        if removed:
            self.save_books(new_books)
            print(f"'{name}' removed successfully.")
        else:
            print("Book not found!")

    # View all books
    def view_books(self):
        books = self.load_books()
        if len(books) == 0:
            print("No books available.")
        else:
            print("\nLibrary Books")
            for b in books:
                print(b)


# Main Menu
library = LMS()

while True:
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. Update Book")
    print("3. Remove Book")
    print("4. View Books")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        name = input("Enter book name: ")
        author = input("Enter author name: ")
        pages = input("Enter number of pages: ")
        library.add_book(name, author, pages)

    elif choice == "2":
        old_name = input("Enter current book name: ")
        new_name = input("Enter new book name: ")
        library.update_book(old_name, new_name)

    elif choice == "3":
        name = input("Enter book name to remove: ")
        library.remove_book(name)

    elif choice == "4":
        library.view_books()

    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please try again.")
