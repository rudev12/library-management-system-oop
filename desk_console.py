import book as Book
from library import Library
from database import Database


db= Database()
l1 = Library("Mumbai Library", "Mumbai",db)


while True:
    print("\n===== LIBRARY MENU =====")
    print("1. Search By Title")
    print("2. Search By Author")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Show All Books")
    print("6. Exit")
    
    choice = input("Enter your Choice:" )
    
    if choice == "1":
        title = input("Enter Book Title: ")
                
        l1.search_by_title(title)
            
        
    elif choice == "2":
        author = input("Enter Author Name: ")
              
        l1.search_by_author(author)

    elif choice == "3":
        try:
           book_id = int(input("Enter Book Id: "))
        except ValueError:
            print("Book Id Cannot be Alphabet, Plz Try Again")
            continue
                
        l1.borrow_book(book_id)
        
    
    elif choice == "4":
        try:
            book_id = int(input("Enter Book Id: "))
        except ValueError:
            print("Book Id Cannot be Alphabet, Plz Try Again")
            continue
                
        l1.return_book(book_id)
                
    elif choice == "5":
         l1.show_all_books()

    elif choice == "6":
         print("Exiting")
         break
       
    else:
        print("Invalid Choice")