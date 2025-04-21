# List to store book details
library = []

# Main program loop
while True:
    print("\n--- Book Management System ---")
    print("""
1. Add Book
2. View Book
3. Update Book
4. Delete Book
5. Exit
""")

    choice = input("Enter your choice: ")

    # Add Book
    if choice == "1":
        print("\n--- Add Book ---")
        book_id = input("Enter book ID: ")

        # Check for duplicate book ID
        if any(book[0] == book_id for book in library):
            print("\nBook ID already exists!")
        else:
            book_name = input("Enter book name: ")
            author_name = input("Enter author name: ")

            # Append book details as a list
            library.append([book_id, book_name, author_name])
            print("\nBook added successfully!")

    # View Books
    elif choice == "2":
        print("\n--- View Books ---")

        if not library:
            print("\nNo books available.")
        else:
            # Use consistent table formatting
            print(f"\n{'Book ID':<15}{'Book Name':<20}{'Author':<20}")
            print("-" * 55)

            for book in library:
                print(f"{book[0]:<20}{book[1]:<20}{book[2]:<20}")

    # Update Book
    elif choice == "3":
        print("\n--- Update Book ---")
        book_id = input("Enter book ID to update: ")

        for book in library:
            if book[0] == book_id:
                book[1] = input("Enter new book name: ")
                book[2] = input("Enter new author name: ")
                print("\nBook updated successfully!")
                break
        else:
            print("\nBook ID not found!")

    # Delete Book
    elif choice == "4":
        print("\n--- Delete Book ---")
        book_id = input("Enter book ID to delete: ")

        for book in library:
            if book[0] == book_id:
                library.remove(book)
                print("\nBook deleted successfully!")
                break
        else:
            print("\nBook ID not found!")

    # Exit
    elif choice == "5":
        print("\nExiting the Book Management System. Goodbye!")
        break

    # Invalid Choice
    else:
        print("\nInvalid choice. Try again.")
