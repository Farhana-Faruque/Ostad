from save_books import save_books
# the title , author(s), ISBN, publishing year, price and quantity information

def add_books(all_books):
    title = input("Enter the book name: ")
    author = input("Enter the author name: ")
    isbn = int(input("Enter the isbn: "))
    year = int(input("Enter the publishing year: "))
    price = int(input("Enter the price: "))
    quantity = int(input("Enter quantity number: "))

    book = {
        "title" : title,
        "author" : author,
        "isbn" : isbn,
        "year" : year,
        "price" : price,
        "quantity" : quantity
    }

    all_books.append(book)
    save_books(all_books)

    print("Books added Successfully")

    return all_books 
