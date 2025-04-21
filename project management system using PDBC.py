import mysql.connector
from datetime import datetime, timedelta

# Establishing the connection to MySQL
def create_connection():
    return mysql.connector.connect(
        host="localhost",        
        user="root",              # Your MySQL username
        password="user123",       # Your MySQL password
        database="python_123"     # The database you're using
    )

# Function to create a task and save it to the database
def create_task(cursor, name, description, deadline, priority):
    query = """INSERT INTO tasks (name, description, deadline, priority, status) 
               VALUES (%s, %s, %s, %s, %s)"""
    values = (name, description, deadline, priority, "Pending")
    cursor.execute(query, values)

# Function to view all tasks
def view_tasks(cursor):
    query = "SELECT * FROM tasks"
    cursor.execute(query)
    tasks = cursor.fetchall()
    for task in tasks:
        # Ensure that each task has the expected number of columns (6 columns)
        if len(task) == 6:
            print(f"Task ID: {task[0]}\nName: {task[1]}\nDescription: {task[2]}\nDeadline: {task[3]}\nPriority: {task[4]}\nStatus: {task[5]}\n")
        else:
            print("Unexpected number of columns in task.")

# Function to update the status of a task (e.g., mark as completed)
def update_task_status(cursor, task_id, status):
    query = "UPDATE tasks SET status = %s WHERE id = %s"
    cursor.execute(query, (status, task_id))

# Function to generate a progress report (count tasks based on status)
def generate_progress_report(cursor):
    query = "SELECT status, COUNT(*) FROM tasks GROUP BY status"
    cursor.execute(query)
    report = cursor.fetchall()
    for status, count in report:
        print(f"Status: {status}, Count: {count}")

# Function to check for due date reminders (tasks with deadlines approaching in 3 days)
def due_date_reminder(cursor):
    current_date = datetime.now().date()  # Use only the date (no time)
    reminder_date = current_date + timedelta(days=3)
    query = "SELECT id, name, deadline FROM tasks WHERE deadline BETWEEN %s AND %s"
    cursor.execute(query, (current_date, reminder_date))
    tasks = cursor.fetchall()
    for task in tasks:
        print(f"Reminder: Task ID: {task[0]}, Name: {task[1]}, Due by: {task[2]}")

# Function to search tasks based on a keyword
def search_tasks(cursor, keyword):
    query = "SELECT * FROM tasks WHERE name LIKE %s OR description LIKE %s"
    cursor.execute(query, ('%' + keyword + '%', '%' + keyword + '%'))
    tasks = cursor.fetchall()
    if tasks:
        for task in tasks:
            print(f"Task ID: {task[0]}\nName: {task[1]}\nDescription: {task[2]}\nDeadline: {task[3]}\nPriority: {task[4]}\nStatus: {task[5]}\n")
    else:
        print("No tasks found with that keyword.")

# Main Program Execution
def run():
    conn = create_connection()
    cursor = conn.cursor()

    while True:
        # Show menu options
        print("\nProject Management System")
        print("1. Create Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Generate Progress Report")
        print("5. Due Date Reminder (Tasks nearing deadline)")
        print("6. Search Tasks")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            # Create Task
            name = input("Enter task name: ")
            description = input("Enter task description: ")
            deadline_str = input("Enter task deadline (YYYY-MM-DD): ")  # Only date format now
            deadline = datetime.strptime(deadline_str, "%Y-%m-%d").date()  # Using .date() to strip time
            priority = input("Enter task priority (High/Medium/Low): ")
            create_task(cursor, name, description, deadline, priority)
            conn.commit()
            print(f"Task '{name}' created successfully!")

        elif choice == "2":
            # View Tasks
            view_tasks(cursor)

        elif choice == "3":
            # Mark Task as Completed
            task_id = int(input("Enter task ID to mark as completed: "))
            update_task_status(cursor, task_id, "Completed")
            conn.commit()
            print(f"Task {task_id} marked as completed!")

        elif choice == "4":
            # Generate Progress Report
            generate_progress_report(cursor)

        elif choice == "5":
            # Due Date Reminder (tasks nearing deadline)
            due_date_reminder(cursor)

        elif choice == "6":
            # Search Tasks
            keyword = input("Enter keyword to search tasks (e.g., task name or description): ")
            search_tasks(cursor, keyword)

        elif choice == "7":
            # Exit
            print("Exiting Project Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

    cursor.close()
    conn.close()

if __name__ == "__main__":
    run()
