# expense_tracker.py
import csv
from datetime import datetime

def add_expense(expenses):
    amount = float(input("Enter amount: "))
    category = input("Enter category (Food/Transport/Entertainment/Other): ")
    description = input("Enter description: ")
    date = datetime.now().strftime("%Y-%m-%d")
    
    expense = {
        "amount": amount,
        "category": category,
        "description": description,
        "date": date
    }
    expenses.append(expense)
    print(f"Expense of Rs{amount} added!")

def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded")
        return
    
    print("\n=== ALL EXPENSES ===")
    for i, exp in enumerate(expenses, 1):
        print(f"{i}. {exp['date']} | {exp['category']} | Rs{exp['amount']} | {exp['description']}")

def view_total(expenses):
    total = sum(exp['amount'] for exp in expenses)
    print(f"\nTotal Spending: Rs{total}")

def view_by_category(expenses):
    categories = {}
    for exp in expenses:
        cat = exp['category']
        categories[cat] = categories.get(cat, 0) + exp['amount']
    
    print("\n=== SPENDING BY CATEGORY ===")
    for cat, amount in categories.items():
        print(f"{cat}: Rs{amount}")

def save_expenses(expenses):
    with open("expenses.csv", "w", newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['date', 'category', 'amount', 'description'])
        writer.writeheader()
        writer.writerows(expenses)
    print("Expenses saved!")

def load_expenses():
    expenses = []
    try:
        with open("expenses.csv", "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                row['amount'] = float(row['amount'])
                expenses.append(row)
    except FileNotFoundError:
        pass
    return expenses

def main():
    expenses = load_expenses()
    
    while True:
        print("\n=== EXPENSE TRACKER ===")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Total Spending")
        print("4. View by Category")
        print("5. Exit")
        
        choice = input("\nEnter choice: ")
        
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            view_total(expenses)
        elif choice == "4":
            view_by_category(expenses)
        elif choice == "5":
            save_expenses(expenses)
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()