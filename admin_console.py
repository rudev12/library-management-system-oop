import book as Book
from library import Library
from database import Database


db= Database()
l1 = Library("Mumbai Library", "Mumbai",db)


while True:
    print("\n===== LIBRARY MENU =====")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Search By Title")
    print("4. Search By Author")
    print("5. Borrow Book")
    print("6. Return Book")
    print("7. Show All Books")
    print("8. Library Statistics")
    print("9. Restore Deleted Books")
    print("10. Exit")
    
    choice = input("Enter your Choice:" )
    
    if choice == "1":
        title = input("Enter a Book Title: ")
        author = input("Enter Author Name: ")
        genre = input("Enter Book Genre: ")
        book = Book.Book(title,author,genre)
        l1.add_book(book)
        
    elif choice == "2":
        try:
            book_id = int(input("Enter Book Id: "))
           
        except ValueError:
            print("Book Id Cannot be Alphabet, Plz Try Again")
            continue
        
        l1.remove_book(book_id)
        
    elif choice == "3":
        title = input("Enter Book Title: ")
        
        l1.search_by_title(title)
    
    elif choice == "4":
        author = input("Enter Author Name: ")
      
        l1.search_by_author(author)
        
    elif choice == "5":
        try:
            book_id = int(input("Enter Book Id: "))
        except ValueError:
            print("Book Id Cannot be Alphabet, Plz Try Again")
            continue
        
        l1.borrow_book(book_id)
        
    elif choice == "6":
        try:
            book_id = int(input("Enter Book Id: "))
        except ValueError:
            print("Book Id Cannot be Alphabet, Plz Try Again")
            continue
        
        l1.return_book(book_id)
        
    elif choice == "7":
        
        l1.show_all_books()
        
    elif choice == "8":
        
        l1.library_stats()
    elif choice == "9":
        try:
            book_id =int(input("Enter Book id :"))
            l1.restore_deleted_book(book_id)
            
        except ValueError:
            print("Book id cannot Be Alphabet")

    elif choice == "10":
        print("Exiting")
        break
    else:
        print("Invalid Choice")