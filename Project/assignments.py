
from db import connect_db
import mysql.connector


def assign_task():
    conn = None
    cursor = None

    try:
        task_id = int(input("Enter task ID: "))
        employee_id = int(input("Enter employee ID: "))

        conn = connect_db()
        if conn is None:
            return

        cursor = conn.cursor()

        # Check whether the task exists
        cursor.execute(
            "SELECT id FROM tasks WHERE id = %s",
            (task_id,)
        )
        if cursor.fetchone() is None:
            print("Task ID not found.")
            return

        # Check whether the employee exists
        cursor.execute(
            "SELECT id FROM employees WHERE id = %s",
            (employee_id,)
        )
        if cursor.fetchone() is None:
            print("Employee ID not found.")
            return

        query = """
        INSERT INTO assigned_tasks (task_id, employee_id)
        VALUES (%s, %s)
        """
        cursor.execute(query, (task_id, employee_id))
        conn.commit()

        print("Task assigned successfully!")

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


def view_assignments():
    conn = None
    cursor = None

    try:
        conn = connect_db()
        if conn is None:
            return

        cursor = conn.cursor()

        query = """
        SELECT employees.name, tasks.title, tasks.status
        FROM assigned_tasks
        JOIN employees
            ON assigned_tasks.employee_id = employees.id
        JOIN tasks
            ON assigned_tasks.task_id = tasks.id
        ORDER BY assigned_tasks.id
        """
        cursor.execute(query)
        assignments = cursor.fetchall()

        if not assignments:
            print("No assignments found.")
            return

        for assignment in assignments:
            print("-" * 35)
            print("Employee Name:", assignment[0])
            print("Task Title:", assignment[1])
            print("Status:", assignment[2])

    except mysql.connector.Error as err:
        print("Database error:", err)

    except Exception as err:
        print("Unexpected error:", err)

    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None and conn.is_connected():
            conn.close()
