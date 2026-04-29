from utils import books
def add_books():
    name=input("Enter the books name:")
    books.append(name)
    print("books added") 







# def add_books():
#     name = input("Enter the book name: ").strip().lower()
#     if name in library_books:
#         print("Book already exists")
#     else:
#         library_books[name] = {"status": "Available", "issued_on": None}
#         print("Book added successfully")