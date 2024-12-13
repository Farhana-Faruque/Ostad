from datetime import datetime, timedelta 
import save_books

def lend_books(all_books):
    search_book = input("Enter book title to borrow: ")
    for book in all_books:
        if book["title"] == search_book :
            name = input("Enter your name: ")
            phone_number = int(input("Enter your phone number: "))
            borrow_amount = int(input("How many books you want to borrow : "))
            book_borrow_at = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            return_time = timedelta(days = 10)

            if book["quantity"] == 0: 
                print("The book is not available")
                return all_books
            else: 
                book["quantity"] = book["quantity"] - borrow_amount 
                save_books.save_all_books(all_books)
                print("Book is lended successfully.")
                return all_books

        
    print("Book is not found")