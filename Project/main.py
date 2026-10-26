
from employees import add_employee, view_employees
from tasks import add_task, view_tasks, update_task_status
from assignments import assign_task, view_assignments
from comments import add_comment


def main():
    while True:
        print("\n" + "=" * 40)
        print("     EMPLOYEE TASK TRACKING SYSTEM")
        print("=" * 40)
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Add Task")
        print("4. View Tasks")
        print("5. Update Task Status")
        print("6. Assign Task")
        print("7. View Assignments")
        print("8. Add Comment")
        print("9. Exit")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                add_employee()
            elif choice == 2:
                view_employees()
            elif choice == 3:
                add_task()
            elif choice == 4:
                view_tasks()
            elif choice == 5:
                update_task_status()
            elif choice == 6:
                assign_task()
            elif choice == 7:
                view_assignments()
            elif choice == 8:
                add_comment()
            elif choice == 9:
                print("Thank you for using Employee Task Tracker!")
                break
            else:
                print("Invalid choice. Enter a number from 1 to 9.")

        except ValueError:
            print("Please enter a valid number.")

        except Exception as err:
            print("Unexpected error:", err)


if __name__ == "__main__":
    main()
