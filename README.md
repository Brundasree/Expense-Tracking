# 💰 Expense Tracker (Python)

A simple command-line Expense Tracker built with Python.  
This program allows users to add expenses, save them to a file, and view a summary of spending by category with remaining budget.

---

## 🚀 Features

- Add new expenses
- Save expenses to CSV file
- Categorize expenses (Food, Home, Work, Fun, Misc)
- View total spending
- View spending by category
- Calculate remaining budget
- Calculate daily budget for the rest of the month

---

## 📂 Project Structure
expense-tracker/
│
├── expense_tracker.py
├── Expense.py
├── expenses.csv
└── README.md

---

## ⚙️ Requirements

- Python 3.9 or higher

No external libraries required (uses only built-in modules).

---

## ▶️ How to Run

1. Clone the repository

```bash
git clone https://github.com/your-username/expense-tracker.git
cd expense-tracker

python expense_tracker.py
```

🎯 Running Expense Tracker!
Enter expense name: Food
Enter expense amount: 100
Select a category:
1. 🍔 Food
2. 🏠 Home
3. 💼 Work
4. 🎉 Fun
5. ✨ Misc

Expenses By Category 📈:
🍔 Food: $100.00
💵 Total Spent: $100.00
✅ Budget Remaining: $1900.00
👉 Budget Per Day: $63.33

🛠 How It Works

Expenses are saved in expenses.csv

Each expense contains:
Name
Amount
Category

The program reads the file and calculates totals.
