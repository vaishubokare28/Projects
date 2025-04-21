import mysql.connector
from datetime import date

# Connect to MySQL
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="user123",
        database="python_123"
    )

# Add New Book
def add_book():
    title = input("Enter book title: ")
    author = input("Enter author's name: ")
    published_date = input("Enter published date (YYYY-MM-DD): ")
    isbn = input("Enter ISBN: ")
    is_available = True

    query = '''
        INSERT INTO books (title, author, published_date, isbn, is_available)
        VALUES (%s, %s, %s, %s, %s)
    '''
    values = (title, author, published_date, isbn, is_available)

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(query, values)
    conn.commit()

    print("Book added successfully.")
    cursor.close()
    conn.close()

# View All Books
def view_books():
    query = "SELECT * FROM books"

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(query)

    books = cursor.fetchall()
    if books:
        for row in books:
            print(f"ID: {row[0]} | Title: {row[1]} | Author: {row[2]} | Published: {row[3]} | ISBN: {row[4]} | Available: {row[5]}")
    else:
        print("No books found.")
    
    cursor.close()
    conn.close()

# Update Book Availability
def update_book_status():
    book_id = int(input("Enter book ID to update: "))
    new_status = input("Is the book available? (True/False): ")
    
    query = "UPDATE books SET is_available = %s WHERE id = %s"
    values = (new_status == 'True', book_id)

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(query, values)
    conn.commit()

    if cursor.rowcount > 0:
        print(f"Book ID {book_id} availability updated.")
    else:
        print(f"No book found with ID {book_id}.")
    
    cursor.close()
    conn.close()

# Delete Book
def delete_book():
    book_id = int(input("Enter book ID to delete: "))
    
    query = "DELETE FROM books WHERE id = %s"
    values = (book_id,)

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(query, values)
    conn.commit()

    if cursor.rowcount > 0:
        print(f"Book ID {book_id} deleted.")
    else:
        print(f"No book found with ID {book_id}.")
    
    cursor.close()
    conn.close()

# Menu system
def menu():
    while True:
        print("\n--- Library Management System ---")
        print("1. Add a New Book")
        print("2. View All Books")
        print("3. Update Book Availability")
        print("4. Delete a Book")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            add_book()
        elif choice == '2':
            view_books()
        elif choice == '3':
            update_book_status()
        elif choice == '4':
            delete_book()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select between 1-5.")

# Run the program
if __name__ == "__main__":
    menu()
