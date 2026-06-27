# persnoal expense tracker

#Fuction For add expenses
def add_expense(expenses):
    item = input("Enter item: ")
    type = input("Enter type: ")
    price = float(input("Enter price: "))
    date = input("Enter date: ")

    expense = {
        "item": item,
        "type": type,
        "price": price,
        "date": date
    }

    expenses.append(expense)
    print("--------Expense Added Successfully!---------")

# function for view epenses
def view_expenses(expenses):
    if not expenses:
        print("No expenses found!")
    else:
        for exp in expenses:
            print("\nItem :", exp["item"])
            print("Type :", exp["type"])
            print("Price:", exp["price"])
            print("Date :", exp["date"])


# function for check sategory or summary of expenses
def category_summary(expenses):
    summary = {}

    for exp in expenses:
        type = exp["type"]
        price = exp["price"]

        if type in summary:
            summary[type] += price
        else:
            summary[type] = price

    print("\nCategory Summary")
    for type in summary:
        print(type, ":", summary[type])

# check budget 
def budget_report(expenses, budget):
    total = 0
    
    for exp in expenses:
        total += exp["price"]

    remaining = budget - total
    percent = (total / budget) * 100

    print("\n===== Budget Report =====")
    print("Total Spent :", total)
    print("Budget      :", budget)
    print("Remaining   :", remaining)
    print("Used        :", round(percent, 2), "%")

    if percent >= 80:
        print("Warning! Budget is almost used.")

# list is create to store data
expenses = []

budget = float(input("Enter Monthly Budget: "))

# while condition for storing data
while True:
    print("\n===== PERSONAL EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Category Summary")
    print("4. Budget Report")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_expense(expenses)

    elif choice == "2":
        view_expenses(expenses)

    elif choice == "3":
        category_summary(expenses)

    elif choice == "4":
        budget_report(expenses, budget)

    elif choice == "5":
        print("======Thank You!======")
        print("EXIT")
        break

    else:
        print("Invalid Choice!")