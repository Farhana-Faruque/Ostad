from datetime import datetime, timedelta 
import save_books

def return_books(all_books):
    search_book = input("Enter book title you want to return: ")
    for book in all_books:
        if book["title"] == search_book:
            return_amount = int(input("How many books you want to return: "))
 
            book["quantity"] = book["quantity"] + return_amount 
            save_books.save_all_books(all_books)
            print("Book is returned successfully.")
            return all_books

    print("Book is not found")