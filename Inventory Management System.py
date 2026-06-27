# Inventory Management System

inventory = []

# Add Product
def add_product():
    pid = input("Enter Product ID: ")
    name = input("Enter Product Name: ")
    qty = int(input("Enter Quantity: "))

    inventory.append({
        "id": pid,
        "name": name,
        "qty": qty
    })

    print("Product Added Successfully!")

# Stock In
def stock_in():
    pid = input("Enter Product ID: ")

    for product in inventory:
        if product["id"] == pid:
            qty = int(input("Enter Quantity to Add: "))
            product["qty"] += qty
            print("Stock Updated!")
            return

    print("Product Not Found!")

# Stock Out
def stock_out():
    pid = input("Enter Product ID: ")

    for product in inventory:
        if product["id"] == pid:
            qty = int(input("Enter Quantity to Remove: "))

            if product["qty"] >= qty:
                product["qty"] -= qty
                print("Stock Removed!")
            else:
                print("Not Enough Stock!")
            return

    print("Product Not Found!")

# View Inventory
def view_inventory():
    if not inventory:
        print("No Products Found!")
        return

    print("\n===== INVENTORY =====")

    for product in inventory:
        print("\nID:", product["id"])
        print("Name:", product["name"])
        print("Quantity:", product["qty"])

# Low Stock Alert
def low_stock_alert():
    found = False

    print("\n===== LOW STOCK ITEMS =====")

    for product in inventory:
        if product["qty"] < 10:
            print(product["id"], "-", product["name"],
                  "- Qty:", product["qty"])
            found = True

    if not found:
        print("No Low Stock Items")

# Report
def generate_report():
    print("\n===== INVENTORY REPORT =====")
    print("Total Products:", len(inventory))

    total_qty = 0

    for product in inventory:
        total_qty += product["qty"]

    print("Total Quantity in Stock:", total_qty)

# Delete Product
def delete_product():
    pid = input("Enter Product ID to Delete: ")

    for product in inventory:
        if product["id"] == pid:
            inventory.remove(product)
            print("Product Deleted Successfully!")
            return

    print("Product Not Found!")

# Main Program
while True:
    print("\n===== INVENTORY MANAGEMENT SYSTEM =====")
    print("1. Add Product")
    print("2. Stock In")
    print("3. Stock Out")
    print("4. View Inventory")
    print("5. Low Stock Alert")
    print("6. Report")
    print("7. Delete Product")
    print("8. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_product()

    elif choice == "2":
        stock_in()

    elif choice == "3":
        stock_out()

    elif choice == "4":
        view_inventory()

    elif choice == "5":
        low_stock_alert()

    elif choice == "6":
        generate_report()

    elif choice == "7":
        delete_product()

    elif choice == "8":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")