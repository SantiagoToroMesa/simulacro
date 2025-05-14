from functions import add_book, search_book, listbooks, remove_book, listforgenre, register_loan, return_book
#search_book, register_loan, return_book, remove_book, list_books_by_genre, list_all_books)
def menu():
    print("Welcome to the library inventory managment!")
    print("1. Add a book")
    print("2. Search for a book")
    print("3  Register book loan. ")
    print("4. Return a book")
    print("5. Remove a book")
    print("6. List all books by genre")
    print("7. List all books")
    print("8. Exit")
    option = input("Select an option: ")
    return option
inventory = []
listgenres = (["FICTION", "NONFICTION", "SCIENCE", "BIOGRAPHY", "CHILDREN"])
while True:
    option = menu()
    if option == "1":
            try:
                print("Adding a book to the library inventory.")
                title = input("Enter the book title: ")
                author = input("Enter the author name: ")
                year = int(input("Enter the publication year: "))
                amount = int(input("Enter the amount of books: "))
                while True:
                    genre = input("Enter the genre: ").upper()
                    if genre not in listgenres:
                        print("Invalid genre. Please select from the following genres:")
                        print(", ".join(listgenres))
                        continue
                    else:
                        inventory = add_book(inventory, title, author, year, genre, amount)
                        break
            except ValueError:
                print("Invalid input. Please enter a valid information.")


    elif option == "2":
        name = input("Enter the book title to search: ")
        print("Searching the book in the library inventory.")
        book = search_book(inventory, name)
        if book:
            print(f"Book found: {book}")
        else:
            print("Book not found in the inventory.")
    elif option == "3":
        book = input("Enter the book title to loan: ")
        print("Registering the book loan.")
        inventory = register_loan(inventory, book)
    elif option == "4":
        book = input("Enter the book title to return: ")
        print("Registering the book return.")
        inventory = return_book(inventory, book)
    elif option == "5":
        title = input("Enter the book title to remove: ")
        remove_book(inventory, title)
    elif option == "6":
        listforgenre(inventory, input("Enter the genre to list: ").upper())
    elif option == "7":
        listbooks(inventory)



