
from db import connect_db
import mysql.connector


def add_employee():
    conn = None
    cursor = None

    try:
        name = input("Enter employee name: ").strip()
        role = input("Enter employee role: ").strip()
        email = input("Enter employee email: ").strip()

        if not name or not email:
            print("Name and email are required.")
            return

        conn = connect_db()
        if conn is None:
            return

        cursor = conn.cursor()

        query = """
        INSERT INTO employees (name, role, email)
        VALUES (%s, %s, %s)
        """
        cursor.execute(query, (name, role, email))
        conn.commit()

        print("Employee added successfully!")

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


def view_employees():
    conn = None
    cursor = None

    try:
        conn = connect_db()
        if conn is None:
            return

        cursor = conn.cursor()
        cursor.execute(
            "SELECT id, name, role, email FROM employees"
        )
        employees = cursor.fetchall()

        if not employees:
            print("No employees found.")
            return

        for employee in employees:
            print(
                f"ID: {employee[0]} | "
                f"Name: {employee[1]} | "
                f"Role: {employee[2]} | "
                f"Email: {employee[3]}"
            )

    except mysql.connector.Error as err:
        print("Database error:", err)

    except Exception as err:
        print("Unexpected error:", err)

    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None and conn.is_connected():
            conn.close()
