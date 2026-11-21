import argparse

all_expenses = []

def add_expense(expense):
    all_expenses.append(expense)
    print(f"expense: {args.add}, description: {args.description}")


parser = argparse.ArgumentParser(prog="expense-tracker")

commands = parser.add_subparsers(dest="command", required=True)

add_parser = commands.add_parser("add", help="add an expense")
add_parser.add_argument("expense")

description_parser = commands.add_parser("--description")
description_parser.add_argument("description")

args = parser.parse_args()

if args.add():
    add_expense