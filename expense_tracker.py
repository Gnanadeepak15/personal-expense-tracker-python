import json
import os

FILE_NAME = "expenses.json"


def load_expenses():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)


def add_expense(expenses):
    category = input("Enter expense category: ")

    try:
        amount = float(input("Enter amount: "))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

    except ValueError:
        print("Please enter a valid amount.")
        return

    expense = {
        "category": category,
        "amount": amount
    }

    expenses.append(expense)
    save_expenses(expenses)

    print("Expense added successfully!")


def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded.")
        return

    for index, expense in enumerate(expenses, start=1):
        print(
            f"{index}. {expense['category']} - "
            f"Rs. {expense['amount']:.2f}"
        )


def show_total(expenses):
    total = sum(expense["amount"] for expense in expenses)
    print(f"Total expenses: Rs. {total:.2f}")


def main():
    expenses = load_expenses()

    while True:
        print("\n--- Personal Expense Tracker ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Show Total Expenses")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            show_total(expenses)
        elif choice == "4":
            print("Thank you for using Expense Tracker!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
