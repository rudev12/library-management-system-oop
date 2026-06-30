class Library:
    def __init__(self, library_name, address):
        self.library_name = library_name
        self.address = address
        self.books = {}
        self.number_employees = 0

    def show_library(self):
        print("Name of library:",self.library_name)
        print("Address:",self.address)
        print("Total Books:",len(self.books))
        print("Total Employee Working:", self.number_employees)
        
    def add_book(self,book):
        if book.book_id in self.books:
            print("Book Alredy Exists, Please Enter Valid Book Id")
        else:
            self.books[book.book_id] = book
            self.save_books()
            print("Book Added Successfully")
        
    def search_book(self,book_id):
        if book_id not in self.books:
            print("Book Id Not Exists Please Enter Valid Id")
        else:
            return self.books[book_id]
            
    def remove_book(self,book_id):
        if book_id not in self.books:
            print("Book Id Not Exists Please Enter Valid Id")
        else:
            book = self.books[book_id]
            self.save_deleted_book(book)
            del self.books[book_id]
            print("Book Removed Successfully")
            self.save_books()

    def show_all_books(self):
        if len(self.books) == 0:
            print("No Books Available In Library")
        else:
            for book in self.books.values():
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
            
    def search_by_title(self,book_title):
        matched_book = []
        
        if book_title.strip()== "":
            print("Title Cannot Be Empty")
        else:
            for book in self.books.values():
                if book_title.lower() in book.title.lower():
                    matched_book.append(book)

        if len(matched_book) == 0:
            print("No Book Found")
        else:
            print("Total Books Found:",len(matched_book))
            for book in matched_book:
                book.show_book()
        return matched_book
        
        
    def search_by_author(self,author):
        matched_author = []
        if author.strip() == "":
            print("Author Name Cannot Be Empty")
            return []
            
        for book in self.books.values(): 
            if author.lower() in book.author.lower():
                matched_author.append(book)
                
        
        if len(matched_author) == 0:
            print("No Author's Book Found")
        else:
            print("Total Books By Author :",(len(matched_author)))
            for book in matched_author:
                book.show_book()
        
        return matched_author
    
    def check_availability(self,book_id):
        book = self.search_book(book_id)
        if book is not None:
            if book.available:
                print(book_id,":","Book is Available")
            else:
                print(book_id,":","Book Not Available")
  
    def load_book(self):
        try:
            with open("library_data.txt","r") as file:
                for line in file:
                    data = line.strip().split(",")
                    if len(data) == 4:
                        book_id, title, author, available = data
                        book = Book(int(book_id),title,author,available = available == "True")
                        self.books[int(book_id)] = book
                    else:
                        print("Invalid data format in line:", line)
                        continue
        except FileNotFoundError:
            print("No Book Data Found")

    def borrow_book(self,book_id):
        if book_id not in self.books:
            print("Book Not Exist")
        else:
            book = self.search_book(book_id)
            if book.available:
                book.available = False
                self.save_books()
                print("Book Borrowed Successfully")
            else:
                print("Book already borrowed.")

    def return_book(self,book_id):
        if book_id not in self.books:
            print("Book Not Exist")
        else:
            book = self.search_book(book_id)
            if not book.available :
                book.available = True
                self.save_books()
                print("Book Returned Successfully")
            else:
                print("Book already Returned .")

    def save_books(self):
        with open("library_data.txt","w") as file:
                    for b in self.books.values():
                        file.write(f"{b.book_id},{b.title},{b.author},{b.available}\n")
                    print("Book Data Saved Successfully")
    
    def update_title(self,book_id,new_title):
        if book_id not in self.books:
            print("Book Not Exist")
        else:
            book = self.search_book(book_id)
            book.update_title(new_title)
            self.save_books()

    def generate_book_id(self):
        if len(self.books) == 0:
            return 101
        
        return max(self.books.keys()) +1 

    def save_deleted_book(self,book):
        with open("deleted_books.txt","a") as file:
            file.write(f"{book.book_id},{book.title},{book.author},{book.available}\n") 
    
    def load_deleted_books(self):
        deleted_books = []
        try:
            with open("deleted_books.txt","r") as file:
                for line in file:
                    data = line.strip().split(",")
                    if len(data) == 4:
                        book_id ,title,author,available = data
                        book = Book(
                            int(book_id),title,author,available = available =="True"
                            )
                        deleted_books.append(book)
        except FileNotFoundError:
            print("No Deleted Book Found")
        
        return deleted_books
    
    def show_deleted_books(self):
        deleted_books = self.load_deleted_books()
        if not deleted_books:
            print("No Deleted Book Found")
        else:
            print("Total Deleted Books:",len(deleted_books))
            for book in deleted_books:
                book.show_book()

    def restore_deleted_book(self, book_id):
        deleted_books = self.load_deleted_books()

        if not deleted_books:
            print("No Book Found In Deleted Books")
            return
        found = False

        for book in deleted_books:

            if book.book_id == book_id:
                found = True
                if book.book_id in self.books:
                    print("Book Already In Library")
                    return

                print("\nBook Found")
                book.show_book()

                confirmation = input(
                    "Are you sure you want to restore this book? (yes/no): "
                    )

                if confirmation.lower() == "yes":
                    self.books[book.book_id] = book
                    self.save_books()
                    deleted_books.remove(book)
                    with open("deleted_books.txt", "w") as file:
                        for b in deleted_books:
                            file.write(
                                f"{b.book_id},{b.title},{b.author},{b.available}\n"
                            )

                    print("Book Restored Successfully")

                elif confirmation.lower() == "no":
                    print("Restoration Cancelled")

                else:
                    print("Invalid Input")

                return

        if not found:
            print("Book Id Not Found")

    def restore_all_deleted_books(self):
        deleted_books = self.load_deleted_books()
        if not deleted_books:
            print("No Deleted Book Found")
        else:
            for book in deleted_books:
                if book.book_id not in self.books:
                    self.books[book.book_id] = book
            self.save_books()
class Book:
    def __init__(self,book_id,title,author,available = True):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = available
    def show_book(self):
        print("=====Book-Info=====")
        print("Book Id:",self.book_id)
        print("Title:",self.title)
        print("Author:",self.author)
        print("Available:",self.available)
        
l1 = Library("Mumbai Library", "Mumbai")
l1.load_book()
l1.load_deleted_books()
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
        book_id = l1.generate_book_id()
        print("Genrated Book Id:",book_id)
        title = input("Enter a Book Title: ")
        author = input("Enter Author Name: ")
        book = Book(book_id,title,author)
        l1.add_book(book)
        
    elif choice == "2":
        try:
            book_id = int(input("Enter Book Id: "))
        except ValueError:
            print("Book Id Cannot be Alphabet, Plz Try Again")
            continue
        
        l1.remove_book(book_id)
        
    elif choice == "3":
        book_title = input("Enter Book Title: ")
        
        l1.search_by_title(book_title)
    
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
