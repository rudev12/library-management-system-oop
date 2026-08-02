import book as Book
import database as db
class Library:
    def __init__(self, library_name, address,db):
        self.library_name = library_name
        self.address = address
        self.books = {}
        self.db =db
        self.number_employees = 0

    def show_library(self):
        print("Name of library:",self.library_name)
        print("Address:",self.address)
        print("Total Books:",len(self.books))
        print("Total Employee Working:", self.number_employees)
        
    def add_book(self, book):
        if self.db.book_checking(book.title,book.author):
            print("Book Already Exisit")
        else:
            self.db.insert_book(
            book.title,
            book.author,
            book.genre)
            print("Book Added Successfully")
        
    def search_book(self,book_id):
        if book_id not in self.books:
            print("Book Id Not Exists Please Enter Valid Id")
        else:
            return self.books[book_id]
            
    def remove_book(self,book_id):
       if not self.db.book_id_checking(book_id):
           print("Book Not Found")
           return
       else:
           while True:
            confirmation = input(
            "Are You Sure You Want To Delete This Book? (yes/no): "
            )
            if confirmation.lower() =="yes":
                succes = self.db.move_to_deleted_books(book_id)
                if succes:
                      print("Book Deleted Succesfully")
                      break
                else:
                    print("Book Deletion Failed")
                    
            elif confirmation.lower() =="no":
                print("Action cancelled!")
                break
            else:
                print("Invalid Input Plz,Try Again!")
     
    def show_all_books(self):
        books =self.db.fetch_books()

        if len(books)==0:
            print("No Books Available in Library")
        else:
            for book in books:
                book.show_book()
                
    def library_stats(self):
        if len(self.books) == 0:
            print("No Books Available in library")
        else:
            total_books = len(self.books)
            available_books = 0
            for book in self.books.values():
                if book.available :
                    available_books += 1
                    
            borrowed_books = total_books - available_books
    
            print("Total Books:",total_books)
            print("Total Available Books:",available_books)
            print("Total Borrowed Books:",borrowed_books)
            
    def search_by_title(self,title):
        books = self.db.check_by_title(title)
        if not books:
            print("Book Not Found")
        else:
            for book in books:
               book.show_book()
        
    def search_by_author(self,author):
       books = self.db.check_by_author(author)
       if not books:
          print("Book Not Found")
       else:
          for book in books:
            book.show_book()

    def check_availability(self,book_id):
        if not self.db.book_id_checking(book_id):
            print("Book Not Found")
            return
        
        if self.db.book_availability_checking(book_id):
            print("Book Is Available")
        else:
            print("Book Id Borrowed")

    def borrow_book(self,book_id):
        if not self.db.book_id_checking(book_id):
            print("Book Not Found")
            return
        
        if not self.db.book_availability_checking(book_id):
            print("Book Already Borrowed")
            return

        self.db.update_availability(book_id,"Borrowed")
        print("Book Borrowed Successfully")

    def return_book(self,book_id):
        if not self.db.book_id_checking(book_id):
            print("Book Not Found")
            return
        if self.db.book_availability_checking(book_id):
            print("Book Already Available")
            return
        self.db.update_availability(book_id,"Available")
        print("Book Returned Successfully")

    def restore_deleted_book(self, book_id):
        if self.db.book_id_checking(book_id):
            print("Book Not Found")
            return
        else:
            while True:
               confirmation = input(
                   "Are You Sure You Want To Restor This Book(yes/no)"
                    )
               if confirmation.lower() =="yes":
                    self.db.restore_deleted_books(book_id)
                    print("Book Restore Succesfully")
                    break
               elif confirmation.lower() == "no":
                    print("Action cancelled!")
                    break
               else:
                    print("Invalid Input,Try Again!")
