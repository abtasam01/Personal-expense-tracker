import json 

class ExpenseManager:
    def __init__(self):
        self.expenses = []

    def load_expenses(self):
        try:
            with open('expenses.json', 'r') as f:
                return json.load(f)
        except: 
            return {}
    
    def save_expenses(self, expenses):
        with open('expenses.json', 'w') as f:
            json.dump(expenses, f)