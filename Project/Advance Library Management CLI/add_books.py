from save_books import save_all_books
import random
from datetime import datetime

def add_books(all_books):
    title = input("Enter the book name: ")
    author = input("Enter the author name: ")
    year = int(input("Enter the publishing year: "))
    price = int(input("Enter the price: "))

    while True: 
        try:
            quantity = int(input("Enter quantity number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    isbn = random.randint(10000,99999)
    bookAddedAt = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    book = {
        "title" : title,
        "author" : author,
        "isbn" : isbn,
        "year" : year,
        "price" : price,
        "quantity" : quantity,
        "bookAddedAt" : bookAddedAt,
        "book_last_update_at" : ""
    }

    all_books.append(book)
    save_all_books(all_books)

    print("Books added Successfully")

    return all_books 