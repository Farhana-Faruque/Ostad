import update_all_books
import restore_all_books_file
import add_books
import view_all_books
import delete_book
import lend_books
import return_books

all_books = []

while True:
    print("Welcome to Library Management System.")
    print("0. Exit ")
    print("1. Add Books")
    print("2. View All Books")
    print("3. Book Update ")
    print("4. Book Remove/ Delete ")
    print("5. Lend books ")
    print("6. Return books ")

    all_books = restore_all_books_file.restore_all_books(all_books)

    menu = input("Select any number: ")

    if menu == "0" :
        print("Thanks for using Library Management System.")
        break
    elif menu == "1" :
        all_books = add_books.add_books(all_books)
    elif menu == "2" :
        view_all_books.view_all_books(all_books)
    elif menu == "3" :
        update_all_books.update_books(all_books)
    elif menu == "4" :
        delete_book.delete_books(all_books)
    elif menu == "5" :
        lend_books.lend_books(all_books)
    elif menu == "6" :
        return_books.return_books(all_books)
    else :
        print("Choose a valid number.")
