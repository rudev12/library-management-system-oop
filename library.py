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
        
            with open("library_data.txt", "a") as file:
                file.write(f"{book.book_id},{book.title},{book.author}\n")
            print("Book Added Successfully")
        
    def search_book(self,book_id):
        if book_id == "    ":
            print("Book Id Cannot be Empty")
        elif book_id not in self.books:
            print("Book Id Not Exists Please Enter Valid Id")
        else:
            return self.books[book_id]
            
    def remove_book(self,book_id):
        if book_id == "   ":
            print("Book Id Cannot be Empty")
        elif book_id not in self.books:
            print("Book Id Not Exists Please Enter Valid Id")
        else:
            book =self.books[book_id]
            del self.books[book_id]
            print("Book Removed Sucessfully")
            return book
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
                if book.title == book_title:
                    matched_book.append(book)
        
        
        if len(matched_book) == 0:
            print("No Book Found")
        
        return matched_book
        
        
    def search_by_author(self,author):
        matched_author = []
        if author.strip() == "":
            print("Author Name Cannot Be Empty")
            
        for book in self.books.values():
            if book.author == author:
                matched_author.append(book)
        if len(matched_author) == 0:
            print("No Author's Book Found")
        
        return matched_author
    
    def check_availability(self,book_id):
        book = self.search_book(book_id)
        if book is not None:
            if book.available:
                print(book_id,":","Book is Available")
            else:
                print(book_id,":","Book Not Available")
                
    def count_book_by_author(self,author):
        author_count = 0
        if author.strip() == "":
            print("Author Name Cannot Be Empty")
        else:
            for book in self.books.values():
                if book.author == author:
                    author_count += 1 
        
        return author_count
        
    def search_partial_title(self,title):
        matched_book = []
        if title.strip() == "":
            print("Title Cannot Be Empty")
        else:
            for book in self.books.values():
                if title in book.title:
                    matched_book.append(book)
            
        if len(matched_book) == 0:
            print("No Book Found")
            
        return matched_book
    
    def load_book(self):
        try:
            with open("library_data.txt","r") as file:
                for line in file:
                    data = line.strip().split(",")
                    if len(data) == 3:
                        book_id, title, author = data
                        book = Book(int(book_id),title,author)
                        self.books[int(book_id)] = book
                    else:
                        print("Invalid data format in line:", line)
                        continue
        except FileNotFoundError:
            print("No Book Data Found")

class Book:
    def __init__(self,book_id,title,author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True
    def show_book(self):
        print("=====Book-Info=====")
        print("Book Id:",self.book_id)
        print("Title:",self.title)
        print("Author:",self.author)
        print("Available:",self.available)
        
    def borrow_book(self):
        if self.available :
            print("Book Borrowed Successfully")
            self.available = False
        else:
            print("Book Already Borrowed")
            
    def return_book(self):
        if not self.available:
            print("Book Returned Successfully")
            self.available = True
        else:
            print("Book Was Not Borrowed")
    
    def update_title(self, new_title):
        if new_title.strip() == " ":
            print("Title Cannot Be Empty")
        else:
            self.title = new_title
            print("Title Updated Successfully")
            print("Title:",self.title)
        
b1 = Book(101,"Python Basics", "Rudhraksh")
b2 = Book(102,"C++ Basics ","Swayam")
l1 = Library("Mumbai Library", "Mumbai")
l1.load_book()
l1.add_book(b2)
