class Book:
    def __init__(self,title,author,genre,book_id=None,available = True):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.genre = genre
        self.available = available
    def show_book(self):
        print("=====Book-Info=====")
        print("Book Id:",self.book_id)
        print("Title:",self.title)
        print("Author:",self.author)
        print("Genre:",self.genre)
        print("Available:",self.available)
      