from random import choice
from storage import Storage
from datetime import datetime


class ExpenseManager:
    def __init__(self):
        self.storage = Storage()

    
    def add_expense(self):
        id = len(self.storage.expenses) + 1
        amount = float(input("Enter the Amount: "))
        category = input("Enter the Category: ")
        while True:
            date = input("Enter the Date (YYYY-MM-DD): ")
            try:
                datetime.strptime(date, "%Y-%m-%d")
                break
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD format.")

        description = input("Enter the Description: ")
        expense = {
            "id": id,
            "amount": amount,
            "category": category,
            "date": date,
            "description": description
        }
        self.storage.expenses.append(expense)
        self.storage.save_expenses(self.storage.expenses) 
        print("Expense has added successfully.")


    def view_all_expenses(self):
        expenses = self.storage.expenses
        if not expenses:
            print("No expenses found.")
            return

        headers = ("ID", "Amount", "Category", "Date", "Description")
        rows = [
            (
                str(expense["id"]),
                str(expense["amount"]),
                str(expense["category"]),
                str(expense["date"]),
                str(expense["description"]),
            )
            for expense in expenses
        ]

        widths = [
            max(len(headers[i]), max((len(row[i]) for row in rows), default=0))
            for i in range(len(headers))
        ]

        def format_row(cells):
            return " | ".join(cells[i].ljust(widths[i]) for i in range(len(cells)))

        print("\n==== All Expenses ====\n")
        print(format_row(headers))
        print("-+-".join("-" * w for w in widths))
        for row in rows:
            print(format_row(row))
        print()


    def search_id(self, id: int)->bool:
        existing_data = self.storage.expenses
        if id not in [expense["id"] for expense in existing_data]:
            return False
        else:
            return True 


    def search_expenses(self, id: int):
        if self.search_id(id):
            expense = next((expense for expense in self.storage.expenses if expense["id"] == id), None)
            print(expense)
        else:
            print("Expense not found.")


    def edit_expense(self, id: int):
        if self.search_id(id):
            expense = next((expense for expense in self.storage.expenses if expense["id"] == id), None)
            print(expense)
            print("Editing Expense...")
            amount = float(input("Enter the Amount: "))
            category = input("Enter the Category: ")
            while True:
                date = input("Enter the Date (YYYY-MM-DD): ")
                try:
                    datetime.strptime(date, "%Y-%m-%d")
                    break
                except ValueError:
                    print("Invalid date format. Please use YYYY-MM-DD format.")
                    
            description = input("Enter the Description: ")
            expense["amount"] = amount
            expense["category"] = category
            expense["date"] = date
            expense["description"] = description
            self.storage.save_expenses(self.storage.expenses)
            print("Expense updated successfully")
        else:
            print("Expense not found.")

    
    def delete_expense(self, id: int):
        if self.search_id(id):
            expense = next((expense for expense in self.storage.expenses if expense["id"] == id), None)
            self.storage.expenses.remove(expense)
            self.storage.save_expenses(self.storage.expenses)
            print("Expense deleted successfully")
        else:
            print("Expense not found.")

    
    def monthly_summary(self):
        expenses = self.storage.expenses

        if not expenses:
            print("No expenses found.")
            return

        year = int(input("Enter year (YYYY): "))
        month = int(input("Enter month (1-12): "))

        total = 0
        category_summary = {}

        for expense in expenses:
            expense_date = datetime.strptime(expense["date"], "%Y-%m-%d")

            if expense_date.year == year and expense_date.month == month:
                total += expense["amount"]

                category = expense["category"]
                category_summary[category] = (
                    category_summary.get(category, 0) + expense["amount"]
                )

        if total == 0:
            print(f"No expenses found for {year}-{month:02d}")
            return

        print(f"\n===== Monthly Summary ({year}-{month:02d}) =====")

        for category, amount in category_summary.items():
            print(f"{category.capitalize():15} ₹{amount:.2f}")

        print("-" * 30)
        print(f"Total Expenses: ₹{total:.2f}")


    def category_summary(self):
        expenses = self.storage.expenses
        if not expenses:
            print("No expenses found.")
            return
        category_summary = {}

        for expense in expenses:
            category = expense["category"]
            category_summary[category] = (
                category_summary.get(category, 0) + expense["amount"]
            )

        print("\n===== Category Summary =====")
        for category, amount in category_summary.items():
            print(f"{category.capitalize():15} ₹{amount:.2f}")

        print("-" * 30)
        print(f"Total Expenses: ₹{sum(category_summary.values()):.2f}")

            
    

        
            
               



    