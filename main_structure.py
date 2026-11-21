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

add_parser = commands.add_parser("add", help="add an expense")
add_parser.add_argument("expense")

description_parser = commands.add_parser("--description")
description_parser.add_argument("description")

args = parser.parse_args()

if args.add():
    add_expense