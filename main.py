from utils import books, issued_books
from add_book import add_books
from show_book import show_books
from issue_book import issue_books
from rtn_book import return_books

def library():
    while True:
        print("1.Add Books")
        print("2.Show Books")
        print("3.Issue Books")
        print("4.Return Books")
        print("5.Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_books()
        elif choice == "2":
            show_books()
        elif choice == "3":
            issue_books()
        elif choice == "4":
            return_books()
        elif choice == "5":
            print("Thank You")
            break
        else:
            print("Invalid choice")

library()
