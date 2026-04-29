from utils import books,issued_books
def issue_books():
    name=input("Enter the book name:")
    if name in books:
        books.remove(name)
        issued_books.append(name)
        print("Book Issued")
    else:
        print("Book not available")
