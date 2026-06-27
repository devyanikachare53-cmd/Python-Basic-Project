# Library Management System

library = {}

while True:
    print("\n======= LIBRARY MENU =======")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Search Book")
    print("5. View Catalog")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # Add Book
    if choice == "1":
        isbn = input("Enter ISBN: ")

        if isbn in library:
            print("Book with this ISBN already exists.")
        else:
            title = input("Enter Title: ")
            author = input("Enter Author: ")

            library[isbn] = {
                "title": title,
                "author": author,
                "available": True,
                "borrower": None,
                "issue_date": None
            }

            print("-------Book added successfully.--------")

    # Issue Book
    elif choice == "2":
        isbn = input("Enter ISBN to issue: ")

        if isbn not in library:
            print("Book not found.")
        else:
            book = library[isbn]

            if book["available"]:
                borrower = input("Enter borrower name: ")
                issue_date = input("Enter issue date (DD-MM-YYYY): ")

                book["available"] = False
                book["borrower"] = borrower
                book["issue_date"] = issue_date

                print("-------Book issued successfully.--------")
            else:
                print("Book is already issued.")
                print("Borrower:", book["borrower"])

    # Return Book
    elif choice == "3":
        isbn = input("Enter ISBN to return: ")

        if isbn not in library:
            print("Book not found.")
        else:
            book = library[isbn]

            if not book["available"]:
                book["available"] = True
                book["borrower"] = None
                book["issue_date"] = None

                print("-------Book returned successfully.--------")
            else:
                print("Book is not currently issued.")

    # Search Book
    elif choice == "4":
        keyword = input("Enter title/author keyword: ").lower()

        found = False

        for isbn, book in library.items():
            if (keyword in book["title"].lower() or
                    keyword in book["author"].lower()):

                print("\nISBN:", isbn)
                print("Title:", book["title"])
                print("Author:", book["author"])
                print("Available:", book["available"])

                found = True

        if not found:
            print("No matching books found.")

    # View Catalog
    elif choice == "5":
        if not library:
            print("Library catalog is empty.")
        else:
            for isbn, book in library.items():
                status = "Available" if book["available"] else "Issued"

                print("\nISBN:", isbn)
                print("Title:", book["title"])
                print("Author:", book["author"])
                print("Status:", status)
                print("Borrower:", book["borrower"] or "-")
                print("Issue Date:", book["issue_date"] or "-")
                print("-" * 30)
    # Exit
    elif choice == "6":
        print("-------Exiting Library Management System...--------")
        break

    else:
        print("-------Invalid choice. Please try again.-------")