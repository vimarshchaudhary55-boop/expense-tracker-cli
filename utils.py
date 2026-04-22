import json
from datetime import datetime

FILE = "expenses.json"

def load_data():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

def add_expense(amount, category):
    data = load_data()
    expense = {
        "amount": amount,
        "category": category,
        "date": str(datetime.now())
    }
    data.append(expense)
    save_data(data)
    print("Expense added!")

def view_expenses():
    data = load_data()
    if not data:
        print("No expenses found.")
        return

    for exp in data:
        print(f"{exp['date']} | {exp['category']} | ₹{exp['amount']}")

def total_expense():
    data = load_data()
    total = sum(exp["amount"] for exp in data)
    print(f"Total Spending: ₹{total}")
