import mysql.connector

# Establish connection
dbconnection = mysql.connector.connect(
    user='root',
    password='user123',
    host='localhost',
    port=3306,
    database='python_123'
)

# Call cursor
mycursor = dbconnection.cursor()

# Create table (fixed with proper syntax and added commas if required)
mycursor.execute("""
    CREATE TABLE IF NOT EXISTS stud_info (
        id INT PRIMARY KEY,
        name VARCHAR(30),
        city VARCHAR(20),
        institute_name VARCHAR(30),
        course_name VARCHAR(30)
    )
""")
dbconnection.commit()

# Function to insert record
def insert_record(id, name, city, institute_name, course_name):
    sql = "INSERT INTO stud_info (id, name, city, institute_name, course_name) VALUES (%s, %s, %s, %s, %s)"
    values = (id, name, city, institute_name, course_name)
    mycursor.execute(sql, values)
    dbconnection.commit()

# Function to display records
def display_record():
    sql = "SELECT * FROM stud_info"
    mycursor.execute(sql)

    print("id   name   city  institute_name   course_name")
    for row in mycursor:
        print(f"{row[0]}    {row[1]}   {row[2]}    {row[3]}     {row[4]}")

# Function to update record
def update_record(id, city):
    sql = "UPDATE stud_info SET city = %s WHERE id = %s"
    values = (city, id)
    mycursor.execute(sql, values)
    dbconnection.commit()
    print("Record updated successfully")

# Function to delete record
def delete_record(id):
    sql = "DELETE FROM stud_info WHERE id = %s"
    values = (id,)
    mycursor.execute(sql, values)
    dbconnection.commit()
    print("Record deleted successfully")

# Menu loop
while True:
    print("""
    1. Insert Record
    2. Display Records
    3. Update Records
    4. Delete Record
    5. Exit
    """)
    
    ch = int(input("Enter your choice: "))
    
    if ch == 1:
        id = int(input("Enter id: "))
        name = input("Enter name: ")
        city = input("Enter city: ")
        institute_name = input("Enter institute_name: ")
        course_name = input("Enter course_name: ")
        insert_record(id, name, city, institute_name, course_name)
    
    elif ch == 2:
        display_record()
    
    elif ch == 3:
        id = int(input("Enter id: "))
        city = input("Enter new city: ")
        update_record(id, city)
    
    elif ch == 4:
        id = int(input("Enter id: "))
        delete_record(id)

    elif ch == 5:
        print("Exiting program...")
        break
    
    else:
        print("Please enter a valid choice.")
