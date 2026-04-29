from utils import issued_books,books
def return_books():
    name=input("Enter the book name")
    if name in issued_books:
        issued_books.remove(name)
        books.append(name)
        print("Book returned")
    else:
        print("Book not issued") 