import json


class Storage:
    def __init__(self):
        self.expenses = self.load_expenses()

    def load_expenses(self) -> list[dict]:
        with open("expenses.json", "r") as f:
            return json.load(f)

    def save_expenses(self, expenses: list[dict]):
        with open("expenses.json", "w") as f:
            json.dump(expenses, f, indent=4)

    