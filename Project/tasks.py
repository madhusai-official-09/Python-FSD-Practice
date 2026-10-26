
from db import connect_db
import mysql.connector


def add_task():
    conn = None
    cursor = None

    try:
        title = input("Enter task title: ").strip()
        description = input("Enter task description: ").strip()
        due_date = input("Enter due date (YYYY-MM-DD): ").strip()

        if not title:
            print("Task title is required.")
            return

        conn = connect_db()
        if conn is None:
            return

        cursor = conn.cursor()
        query = """
        INSERT INTO tasks (title, description, due_date)
        VALUES (%s, %s, %s)
        """
        cursor.execute(query, (title, description, due_date))
        conn.commit()
        print("Task added successfully!")

    except mysql.connector.Error as err:
        print("Database error:", err)
        if conn is not None and conn.is_connected():
            conn.rollback()

    except ValueError as err:
        print("Invalid input:", err)

    except Exception as err:
        print("Unexpected error:", err)

    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None and conn.is_connected():
            conn.close()


def view_tasks():
    conn = None
    cursor = None

    try:
        conn = connect_db()
        if conn is None:
            return

        cursor = conn.cursor()
        cursor.execute(
            "SELECT id, title, description, status, due_date FROM tasks"
        )
        tasks = cursor.fetchall()

        if not tasks:
            print("No tasks found.")
            return

        for task in tasks:
            print("-" * 35)
            print(f"Task ID: {task[0]}")
            print(f"Title: {task[1]}")
            print(f"Description: {task[2]}")
            print(f"Status: {task[3]}")
            print(f"Due Date: {task[4]}")

    except mysql.connector.Error as err:
        print("Database error:", err)

    except Exception as err:
        print("Unexpected error:", err)

    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None and conn.is_connected():
            conn.close()


def update_task_status():
    conn = None
    cursor = None

    try:
        task_id = int(input("Enter task ID: "))
        status = input(
            "Enter status (Pending/In Progress/Completed): "
        ).strip()

        allowed_statuses = ("Pending", "In Progress", "Completed")

        if status not in allowed_statuses:
            print("Invalid status.")
            return

        conn = connect_db()
        if conn is None:
            return

        cursor = conn.cursor()
        query = "UPDATE tasks SET status = %s WHERE id = %s"
        cursor.execute(query, (status, task_id))
        conn.commit()

        if cursor.rowcount > 0:
            print("Task status updated successfully!")
        else:
            print("Task not found or status unchanged.")

    except ValueError:
        print("Task ID must be a valid number.")

    except mysql.connector.Error as err:
        print("Database error:", err)
        if conn is not None and conn.is_connected():
            conn.rollback()

    except Exception as err:
        print("Unexpected error:", err)

    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None and conn.is_connected():
            conn.close()
