from utils import books,issued_books
def issue_books():
    name=input("Enter the book name:")
    if name in books:
        books.remove(name)
        issued_books.append(name)
        print("Book Issued")
    else:
        print("Book not available")








# def issue_books():
#     name = input("Enter the book name: ").strip().lower()
#     if name in library_books:
#         if library_books[name]["status"] == "Available":
#             library_books[name]["status"] = "Issued"
#             library_books[name]["issued_on"] = datetime.date.today()
#             print("Book issued successfully")
#         else:
#             print("Book is already issued")
#     else:
#         print("Book not found")