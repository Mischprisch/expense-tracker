import json
import argparse
import datetime

with open("expenses.json", "r") as f:
    data = json.load(f)

all_expenses = data

def save_data():
    with open("expenses.json", "w") as f:
        json.dump(all_expenses, f, indent=2)


def add_expense(description,amount):
    if amount <= 0:
        print("Amount cannot be below or equal to €0")
        return
    elif expense in all_expenses:
        return
    expense = {"description":description,"amount":amount}
    all_expenses.append(expense)
    print(f"Expense added successfully (ID: {all_expenses.index(expense) + 1})")
    save_data()


def list_expenses():
    for expense in all_expenses:
        print(expense)


def summary():
    total = sum(expense["amount"] for expense in all_expenses)
    print(f"Total expenses: €{total}")


def delete_expense(id):
    try:
        expense = all_expenses[int(id)-1]
        all_expenses.remove(expense)
        print("Expense deleted successfully")
        save_data()
    except IndexError:
        print("List index out of range")




parser = argparse.ArgumentParser(prog="expense-tracker")

commands = parser.add_subparsers(dest="command", required=True)

add_parser = commands.add_parser("add")
add_parser.add_argument("-d","--description")
add_parser.add_argument("-a","--amount", type=float)

list_parser = commands.add_parser("list")

summary_parser = commands.add_parser("summary")

delete_parser = commands.add_parser("delete")
delete_parser.add_argument("-id","--id")

args = parser.parse_args()

if args.command == "add":
    add_expense(args.description,args.amount)
elif args.command == "list":
    list_expenses()
elif args.command == "summary":
    summary()
elif args.command == "delete":
    delete_expense(args.id)