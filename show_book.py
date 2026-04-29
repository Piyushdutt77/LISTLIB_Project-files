from utils import books
def show_books():
    if len(books) == 0:
        print("No Books available")
    else:
        print("Books available")
        for b in books:
            print(b)
