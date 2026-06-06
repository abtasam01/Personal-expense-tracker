import json
from storage import Storage
from expense_manager import ExpenseManager

em = ExpenseManager()


def main():
    print("==== Personal Expense Tracker ====\n")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Search Expenses")
    print("4. Edit Expenses")
    print("5. Delete Expenses")
    print("6. Monthly Summary")
    print("7. Category Summary")
    print("8. Highest Expense")
    print("9. Lowest Expense")
    print("10. Exit")
    while True:
        choice = int(input("Enter your choice: "))
        match choice:
            case 1:
                print("Adding Expense...")
                em.add_expense()
                print("Expense added successfully")
            case 2:
                em.view_all_expenses()
            case 3:
                print("Search Expenses")
            case 4:
                print("Edit Expenses")
            case 5:
                print("Delete Expenses")
            case 6:
                print("Monthly Summary")
            case 7:
                print("Category Summary")
            case 8:
                print("Highest Expense")
            case 9:
                print("Lowest Expense")
            case 10:
                print("Exit")
                break
            case _:
                print("Invalid choice")


if __name__ == "__main__":
    main()
