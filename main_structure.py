import json
import argparse
import datetime as dt

with open("expenses.json", "r") as f:
    data = json.load(f)

all_expenses = data

def save_data():
    with open("expenses.json", "w") as f:
        json.dump(all_expenses, f, indent=2)


def add_expense(description,amount):
    if amount is None or description is None:
        print("Provide a description and an amount")
        return
    if amount <= 0:
        print("Amount cannot be below or equal to €0")
        return
    date = dt.datetime.now()
    date = date.strftime("%d-%m-%Y")
    expense = {"date": date, "description": description, "amount": amount}
    if expense in all_expenses:
        print("Expense already exists")
        return
    all_expenses.append(expense)
    print(f"Expense added successfully (ID: {len(all_expenses)})")


def update_expense(id,description,amount):
    new_date = dt.datetime.now()
    new_date = new_date.strftime("%d-%m-%Y")
    new_expense = {"date": new_date, "description": description, "amount": amount}
    new_description = new_expense["description"]
    new_amount = new_expense["amount"]
    try:
        expense = all_expenses[id-1]
        if new_expense in all_expenses:
            print("Expense already exists")
            return
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
    except IndexError:
        print("list index out of range")

def list_expenses():
    print("ID  Date         Description  Amount\n")
    for expense in all_expenses:
        print(f"{all_expenses.index(expense) + 1}   {expense["date"]}   {expense["description"]}  €{expense["amount"]}")


def summary(month):
    if month == None:
        total = sum(expense["amount"] for expense in all_expenses)
        print(f"Total expenses: €{total}")
        return
    if len(month) == 1:
        month = "0" + month
    try:
        if int(month) < 1 or int(month) > 12:
            print("Put in a number between 1 and 12")
            return
    except ValueError:
        print("Put in a number between 1 and 12")
        return
    for expense in all_expenses:
        m = expense["date"][3] + expense["date"][4]
        d = dt.datetime.strptime(f"{month}", "%m")
        d = d.strftime("%B")
        total = sum(expense["amount"] for expense["date"][m] in all_expenses)
    print(f"Total expenses for {d}: €{round(total, 2)}")



def delete_expense(id):
    try:
        expense = all_expenses[int(id)-1]
        all_expenses.remove(expense)
        print("Expense deleted successfully")
    except IndexError:
        print("list index out of range")


def main():
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
    summary_parser.add_argument("-m","--month")

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
        summary(args.month)
    elif args.command == "delete":
        delete_expense(args.id)
        save_data()


if __name__ == "__main__":
    main()