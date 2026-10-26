
from db import connect_db
import mysql.connector


def add_comment():
    conn = None
    cursor = None

    try:
        task_id = int(input("Enter task ID: "))
        employee_id = int(input("Enter employee ID: "))
        comment_text = input("Enter your comment: ").strip()

        if not comment_text:
            print("Comment cannot be empty.")
            return

        conn = connect_db()
        if conn is None:
            return

        cursor = conn.cursor()

        # Validate task ID
        cursor.execute(
            "SELECT id FROM tasks WHERE id = %s",
            (task_id,)
        )
        if cursor.fetchone() is None:
            print("Task ID not found.")
            return

        # Validate employee ID
        cursor.execute(
            "SELECT id FROM employees WHERE id = %s",
            (employee_id,)
        )
        if cursor.fetchone() is None:
            print("Employee ID not found.")
            return

        query = """
        INSERT INTO comments (task_id, employee_id, comment_text)
        VALUES (%s, %s, %s)
        """
        cursor.execute(
            query, (task_id, employee_id, comment_text)
        )
        conn.commit()

        print("Comment added successfully!")

    except ValueError:
        print("Task ID and Employee ID must be numbers.")

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
