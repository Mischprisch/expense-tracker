import json
import argparse
import datetime

with open("expenses.json", "r") as f:
    data = json.load(f)

all_expenses = data

def add_expense(description,amount):
    expense = {"description":description,"amount":amount}
    if expense in all_expenses:
        return
    all_expenses.append(expense)
    print(f"Expense added successfully (ID: {all_expenses.index(expense)+1})")
    with open("expenses.json", "w") as f:
        json.dump(all_expenses, f, indent=2)


def list_expenses():
    for expense in all_expenses:
        print(expense)


parser = argparse.ArgumentParser(prog="expense-tracker")

commands = parser.add_subparsers(dest="command", required=True)

add_parser = commands.add_parser("add")
add_parser.add_argument("-d","--description")
add_parser.add_argument("-a","--amount")

list_parser = commands.add_parser("list")


args = parser.parse_args()

if args.command == "add":
    add_expense(args.description,args.amount)
elif args.command == "list":
    list_expenses()