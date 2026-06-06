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

    

    