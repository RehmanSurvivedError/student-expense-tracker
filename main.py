from expense_manager import (
    add_expense,
    view_expenses,
    search_expense,
    delete_expense
)

from reports import (
    total_expenses,
    category_summary,
    monthly_summary
)


def show_menu():
    print("\t\t\t===== Student Expense Tracker =====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Search Expenses")
    print("4. Delete Expense")
    print("5. Show All Expenses")
    print("6. Category Summary")
    print("7. Monthly Summary")
    print("8. Exit")

    try:
        choice = int(input("Enter your choice: "))
        if 1 <= choice <= 8:
            return choice
        else:
            print("Invalid choice. Please select between 1 and 8.")
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 8")
        
def main():
    while True:
        choice = show_menu()

        if choice == 1:
            add_expense()

        elif choice == 2:
            view_expenses()

        elif choice == 3:
            search_expense()

        elif choice == 4:
            delete_expense()

        elif choice == 5:
            total_expenses()

        elif choice == 6:
            category_summary()

        elif choice == 7:
            monthly_summary()
        elif choice == 8:
            print("Thank you for using Student Expense Tracker.")
            break


if __name__ == "__main__":
    main()