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
    if amount is None or description is None:
        print("Provide a description and a amount")
        return
    if amount <= 0:
        print("Amount cannot be below or equal to €0")
        return
    expense = {"description": description, "amount": amount}
    if expense in all_expenses:
        print("Expense already exists")
        return
    all_expenses.append(expense)
    print(f"Expense added successfully (ID: {all_expenses.index(expense) + 1})")


def update_expense(id,description,amount):
    new_expense = {"description": description, "amount": amount}
    new_description = new_expense["description"]
    new_amount = new_expense["amount"]
    expense = all_expenses[id-1]
    if description and amount is None:
        expense["description"] = new_description
        print("Expense description updated successfully")
        return
    if amount and description is None:
        expense["amount"] = new_amount
        print("Expense amount updated successfully")
        return
    elif description is None and amount is None:
        print("Input a value please")
        return
    else:
        all_expenses[id-1] = new_expense
        print("Expense updated successfully")


def list_expenses():
    print("ID  Description  Amount")
    for expense in all_expenses:
        print(f"{all_expenses.index(expense) + 1}   {expense["description"]}  €{expense["amount"]}")


def summary():
    total = sum(expense["amount"] for expense in all_expenses)
    print(f"Total expenses: €{total}")


def delete_expense(id):
    try:
        expense = all_expenses[int(id)-1]
        all_expenses.remove(expense)
        print("Expense deleted successfully")
    except IndexError:
        print("List index out of range")


parser = argparse.ArgumentParser(prog="expense-tracker")

commands = parser.add_subparsers(dest="command",required=True)

add_parser = commands.add_parser("add")
add_parser.add_argument("-d","--description")
add_parser.add_argument("-a","--amount",type=float)

update_parser = commands.add_parser("update")
update_parser.add_argument("-id","--id",type=int)
update_parser.add_argument("-d","--description")
update_parser.add_argument("-a","--amount",type=float)

list_parser = commands.add_parser("list")

summary_parser = commands.add_parser("summary")

delete_parser = commands.add_parser("delete")
delete_parser.add_argument("-id", "--id")

args = parser.parse_args()

if args.command == "add":
    add_expense(args.description,args.amount)
    save_data()
elif args.command == "update":
    update_expense(args.id,args.description,args.amount)
    save_data()
elif args.command == "list":
    list_expenses()
elif args.command == "summary":
    summary()
elif args.command == "delete":
    delete_expense(args.id)
    save_data()