from file_handler import load_expenses, save_expenses

def validate_amount(amount: float)-> bool:
    if amount <= 0:
        print("Amount must be greater than zero.")
        return False
    return True

def add_expense():

    expenses = load_expenses()
    try:
        amount = float(input("Enter expense amount: "))
    except ValueError:
        print("Invalid amount. Please enter a valid number.")
    else:
        if not validate_amount(amount):
            return
        category = input("Enter expense category: ")
        date = input("Enter expense date (YYYY-MM-DD): ")
        description = input("Enter expense description: ")

        expense =  {
                "amount":amount,
                "category":category,
                "date":date,
                "description":description
            }

        expenses.append(expense)
        save_expenses(expenses)
        print("Expense added successfully!")

def view_expenses():
    expenses = load_expenses()
    if not expenses:
        print("No expenses found.")
        return

    print("\n===== All Expenses =====")
    for idx, expense in enumerate(expenses, start=1):
        print(f"{idx}. {expense['date']} | {expense['category']} | ${expense['amount']:.2f} | {expense['description']}")

def delete_expense():
    expenses = load_expenses()
    if not expenses:
        print("No expenses to delete.")
        return

    view_expenses()
    try:
        idx = int(input("Enter the number of the expense to delete: "))
        if 1 <= idx <= len(expenses):
            deleted_expense = expenses.pop(idx - 1)
            save_expenses(expenses)
            print(f"Deleted expense: {deleted_expense['description']} | (${deleted_expense['amount']:.2f})")
        else:
            print("Invalid number. Please select a valid expense.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def search_expense():
    expenses = load_expenses()
    if not expenses:
        print("No expenses to search.")
        return
    keyword = input("Enter amount to search: ")
    found_expenses = [expense for expense in expenses if keyword in str(expense['amount'])]

    if not found_expenses:
        print("No expenses found.")
    else:
        print("\n===== Search Results =====")
        for idx, expense in enumerate(found_expenses, start=1):
            print(f"{idx}. {expense['date']} | {expense['category']} | ${expense['amount']:.2f} | {expense['description']}")

        
        

