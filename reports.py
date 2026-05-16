from file_handler import load_expenses


def total_expenses():
    expenses = load_expenses()

    total = 0

    for expense in expenses:
        total += expense["amount"]

    print(f"\nTotal Expenses: {total}")


def category_summary():
    expenses = load_expenses()

    summary = {}

    for expense in expenses:
        category = expense["category"]

        if category in summary:
            summary[category] += expense["amount"]
        else:
            summary[category] = expense["amount"]

    print("\n===== Category Summary =====")

    for category, total in summary.items():
        print(f"{category}: {total}")


def monthly_summary():
    expenses = load_expenses()

    month = input("Enter month (e.g., 2026-05): ")

    total = 0

    for expense in expenses:
        if expense["date"].startswith(month):
            total += expense["amount"]

    print(f"\nTotal for {month}: {total}")