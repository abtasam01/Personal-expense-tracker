# Personal Expense Tracker

A command-line personal finance application built with Python. Record daily spending, manage your expense history, and get useful summaries — all stored locally in a JSON file.

This project demonstrates modular Python design by separating the user interface, business logic, and data persistence into dedicated files.

---

## Features

### Expense Management
- **Add Expense** — Log a new expense with amount, category, date, and description. Each entry is assigned a unique ID and saved automatically.
- **View All Expenses** — Display every saved expense in a clean, readable list with full details.
- **Search Expenses** — Find expenses by keyword, category, date, or description.
- **Edit Expenses** — Update an existing expense by ID (amount, category, date, or description).
- **Delete Expenses** — Remove an expense by ID with confirmation.

### Reports & Analytics
- **Monthly Summary** — View total spending for any month, with a count of expenses recorded.
- **Category Summary** — See how much you spent in each category and compare spending habits.
- **Highest Expense** — Quickly identify your single largest expense.
- **Lowest Expense** — Quickly identify your single smallest expense.

### General
- **Persistent Storage** — All data is saved to `expenses.json` and restored when the app starts.
- **Interactive CLI Menu** — Simple numbered menu that loops until you choose Exit.
- **Input Validation** — Handles invalid menu choices and guides the user with clear messages.

---

## Project Structure

```
Personal expense tracker/
├── main.py              # Entry point — menu, user input, calls ExpenseManager
├── expense_manager.py   # Business logic — CRUD operations and reports
├── storage.py           # File operations — load/save expenses.json
├── expenses.json        # Stored expense data
├── .gitignore
└── README.md
```

| File | Responsibility |
|------|----------------|
| `main.py` | User interface — prints menu, reads choices, delegates to the manager |
| `expense_manager.py` | Expense logic — add, view, search, edit, delete, summaries |
| `storage.py` | Persistence — reads and writes `expenses.json` |
| `expenses.json` | Data file — list of expense records |

---

## Requirements

- Python 3.10+ (uses `match` / `case`)
- No external packages required (built-in `json` module only)

---

## How to Run

1. **Open the project folder**

2. **Create and activate a virtual environment** (recommended)

   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

3. **Start the application**

   ```powershell
   python main.py
   ```

4. **Select an option** — enter a number from 1 to 10.

---

## Menu Options

| # | Option | Description |
|---|--------|-------------|
| 1 | Add Expense | Record a new expense |
| 2 | View All Expenses | List every saved expense |
| 3 | Search Expenses | Find expenses by keyword or filter |
| 4 | Edit Expenses | Update an existing expense by ID |
| 5 | Delete Expenses | Remove an expense by ID |
| 6 | Monthly Summary | Total spending for a selected month |
| 7 | Category Summary | Spending breakdown by category |
| 8 | Highest Expense | Show the largest single expense |
| 9 | Lowest Expense | Show the smallest single expense |
| 10 | Exit | Close the application |

---

## Expense Data Format

Each expense is stored as a dictionary inside a JSON list:

```json
[
    {
        "id": 1,
        "amount": "50",
        "category": "food",
        "date": "2026-06-02",
        "description": "lunch"
    }
]
```

| Field | Description |
|-------|-------------|
| `id` | Unique identifier (auto-generated) |
| `amount` | Cost of the expense |
| `category` | Type of spending (e.g. food, transport, clothing) |
| `date` | Date of the expense |
| `description` | Short note about the purchase |

---

## How It Works

```
User → main.py → expense_manager.py → storage.py → expenses.json
```

1. On startup, `Storage` loads existing expenses from `expenses.json` into memory.
2. The user selects an option from the menu in `main.py`.
3. `ExpenseManager` runs the logic (add, search, edit, delete, or calculate summaries).
4. `Storage` writes the updated list back to `expenses.json` whenever data changes.

---

## Future Enhancements

Features planned for upcoming versions:

- **Payment Method** — Track how each expense was paid (cash, debit card, credit card, UPI, wallet).
- **Budget Limits** — Set a monthly budget per category and get alerts when you are close to the limit.
- **Recurring Expenses** — Mark subscriptions and bills (rent, Netflix, gym) that repeat every month.
- **Export to CSV** — Download expense data for use in Excel or Google Sheets.
- **Date Range Reports** — Filter and summarize spending between any two dates.
- **Tags / Labels** — Add custom tags to expenses for more flexible grouping (e.g. `work`, `travel`, `urgent`).
- **Sorting Options** — Sort expenses by amount, date, or category when viewing the list.
- **Data Backup & Restore** — Create timestamped backups of `expenses.json` and restore from a previous copy.
- **Charts & Visual Reports** — Generate simple bar or pie charts for category spending.
- **App Password Protection** — Optional PIN or password to open the tracker.
- **Multi-Currency Support** — Record expenses in different currencies with a default home currency.

---

## Author

Abtasam Mumtaz Khan — personal learning project built as a second Python project after a password manager.
