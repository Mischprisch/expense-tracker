import argparse

all_expenses = []

def add_expense(description,amount):
    all_expenses.append({description,amount})
    print(f"Expense added successfully (ID:{all_expenses.index({description,amount})+1})")


def list_expenses():
    for expense in all_expenses:
        print(expense)


parser = argparse.ArgumentParser(prog="expense-tracker")

commands = parser.add_subparsers(dest="command", required=True)

add_parser = commands.add_parser("add")
add_parser.add_argument("--description")
add_parser.add_argument("--amount")

list_parser = commands.add_parser("list")


args = parser.parse_args()

if args.add():
    add_expense