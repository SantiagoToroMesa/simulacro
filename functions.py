def add_book(invent, title, author, year, genre, amount):
    invent.append({"title": title, "author": author, "amount": amount, "genre": genre, "year": year})
    print(f"{amount} Book(s) '{title}' by {author} ({year}) in {genre} genre added to the inventory.")
    return invent

def search_book(invent, title):
    for book in invent:
        if book["title"].lower() == title.lower():
            return book
    return None
def remove_book(invent, title):
    for book in invent:
        if book["title"].lower() == title.lower():
            invent.remove(book)
            print(f"Book '{title}' removed from the inventory.")
            return invent
    print(f"Book '{title}' not found in the inventory.")
    return invent
def listbooks(invent):
    print("=" * 40, "INVENTORY", "=" * 40)
    if not invent:
        print("No books in the inventory.")
        print("=" * 91)
        return
    for book in invent:
        print(f"Title: {book['title']}, Author: {book['author']}, Year: {book['year']}, Genre: {book['genre']}, Amount: {book['amount']}")
    print("=" * 91)
def listforgenre(invent, genre):
    listgenres = (["FICTION", "NONFICTION", "SCIENCE", "BIOGRAPHY", "CHILDREN"])
    for genres in listgenres:
        if genre == genres:
            for book in invent:
                print(f"Books in {genre} genre:")
                if book["genre"].lower() == genre.lower():
                    print(f"Title: {book['title']}, Author: {book['author']}, Year: {book['year']}, Amount: {book['amount']}")
            return
        if not invent:
            print("No books in the inventory.")
            return
def register_loan(invent, title):
    for book in invent:
        if book["title"].lower() == title.lower():
            if book["amount"] > 0:
                book["amount"] -= 1
                print(f"Book '{title}' loaned out. Remaining amount: {book['amount']}")
            else:
                print(f"Book '{title}' is not available for loan.")
            return invent
    print(f"Book '{title}' not found in the inventory.")
    return invent

def return_book(invent, title):
    for book in invent:
        if book["title"].lower() == title.lower():
            book["amount"] += 1
            print(f"Book '{title}' returned. Total amount: {book['amount']}")
            return invent
    print(f"Book '{title}' not found in the inventory.")
    return invent