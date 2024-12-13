import save_books

def delete_books(all_books):
    search_book = input("Enter book title to Delete : ")
    for book in all_books:
        if book["title"] == search_book :
            all_books.remove(book)
            save_books.save_all_books(all_books)
            print("Book is deleted successfully")
            return all_books
        
    print("Book is not found")