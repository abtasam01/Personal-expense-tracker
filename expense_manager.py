from storage import Storage


class ExpenseManager:
    def __init__(self):
        self.storage = Storage()
    
    def add_expense(self):
        id = len(self.storage.expenses) + 1
        amount = input("Enter the Amount: ")
        category = input("Enter the Category: ")
        date = input("Enter the Date: ")
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

    def view_all_expenses(self):
        print("====All Expenses====")
        for expense in self.storage.expenses:
            print(f"ID: {expense['id']}")
            print(f"Amount: {expense['amount']}")
            print(f"Category: {expense['category']}")
            print(f"Date: {expense['date']}")
            print(f"Description: {expense['description']}")
            print("-" * 20)

    