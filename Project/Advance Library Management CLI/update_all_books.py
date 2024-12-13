from datetime import datetime
import save_books

def update_books(all_books):
    search_book = input("Enter book title to Update : ")
    for book in all_books:
        if book["title"] == search_book :
            title = input("Enter the book name: ")
            author = input("Enter the author name: ")
            year = int(input("Enter the publishing year: "))
            price = int(input("Enter the price: "))
            quantity = int(input("Enter quantity number: "))

            book_last_update_at = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

            book["title"] = title
            book["author"] = author
            book["year"] = year
            book["price"] = price
            book["quantity"] = quantity
            book["bookAddedAt"] = book_last_update_at 

            save_books.save_all_books(all_books)
            print("Book updated successfully.")
            return all_books
        
    print("Book is not found")