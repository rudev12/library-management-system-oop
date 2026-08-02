import sqlite3
import book as Book

class Database:
   def __init__(self,db_name="library.db"):
      self.db_name = db_name

   def connect(self):
        return sqlite3.connect(self.db_name)
   
   def create_table(self):
       conn = self.connect()
       cursor = conn.cursor()
       cursor.execute("""
CREATE TABLE IF NOT EXISTS books(
                      book_id INTEGER PRIMARY KEY AUTOINCREMENT,
                      title TEXT NOT NULL,
                      author TEXT NOT NULL,
                      genre TEXT,
                      availability TEXT DEFAULT'Available'
    )
    """)
       conn.commit()
       conn.close()

   def create_deleted_books_table(self):
    conn = self.connect()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS deleted_books (
            book_id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            genre TEXT,
            availability TEXT
        )
    """)

    conn.commit()
    conn.close()

    print("Deleted Books Table Created Successfully")

   def insert_book(self, title, author, genre):
       conn = self.connect()
       cursor = conn.cursor()
       cursor.execute("""
INSERT INTO books(title,author,genre)
                      VALUES(?,?,?)
                      """,(title,author,genre))
       book_id = cursor.lastrowid
       print("Book Added Successfully")
       print("Generated Book ID:", book_id)
       
       conn.commit()
       conn.close()

   def fetch_books(self):
       conn = self.connect()
       cursor = conn.cursor()
       cursor.execute("""
SELECT * FROM books;                     
""")
       rows = cursor.fetchall()
       book = []
       for row in rows:
           book_id,title,author,genre,availability = row
           book_object = Book.Book(title,author,genre,book_id,availability)
           book.append(book_object)
       conn.close()
       return book

   def delete_book(self,book_id):
       conn = self.connect()
       cursor = conn.cursor()
       cursor.execute("""
                      DELETE FROM books
                        WHERE book_id =?
                      """,(book_id,))
       if cursor.rowcount == 0:
           print("Book ID Not Found")
       else:
           print("Book Deleted Succesfully")
       conn.commit()
       conn.close()
 
   def update_availability(self,book_id,availability):
       conn =self.connect()
       cursor = conn.cursor()
       cursor.execute("""
UPDATE books
                      SET availability = ?
                      WHERE book_id = ?

""",(availability,book_id))
       if cursor.rowcount == 0:
           conn.close()
           print("Book ID Not Found")
           return False
       else:
           conn.commit()
           conn.close()
           return True

   def update_title(self,book_id,title):
       conn =self.connect()
       cursor = conn.cursor()
       cursor.execute("""
UPDATE books
                      SET title = ?
                      WHERE book_id = ?

""",(title,book_id))
       if cursor.rowcount == 0:
           print("Book ID Not Found")
       else:
           print("Title Updated Succesfully")
       conn.commit()
       conn.close()

   def book_checking(self,title,author):
       conn =self.connect()
       cursor = conn.cursor()
       cursor.execute("""
SELECT *
       FROM books
       WHERE title =?
       And author =?
""",(title,author))
       rows = cursor.fetchall()
       if not rows:
        conn.close()
        return False
       else:
           conn.close()
           return True

   def book_id_checking(self,book_id):
       conn = self.connect()
       cursor = conn.cursor()
       cursor.execute("""
SELECT * 
        FROM books
        WHERE book_id =?
""",(book_id,))
       rows =cursor.fetchall()
       
       if not rows:
           conn.close()
           return False
       else:
           conn.close()
           return True

   def check_by_title(self,title):
       conn = self.connect()
       cursor = conn.cursor()
       search_title = f"%{title}%"
       cursor.execute("""
SELECT *
       FROM books
       WHERE title Like ?
""",(search_title,))
       rows = cursor.fetchall()

       if len(rows) ==0:
           conn.close()
           return False 
       else:
           conn.close()
           return True

   def check_by_author(self,author):
           conn = self.connect()
           cursor = conn.cursor()
           search_author = f"%{author}%"
           cursor.execute("""
    SELECT *
           FROM books
           WHERE author Like ?
    """,(search_author,))
           rows = cursor.fetchall()
    
           if not rows:
               conn.close()
               return False 
           else:
               conn.close()
               return True

   def search_by_title(self,title):
       conn = self.connect()
       cursor = conn.cursor()
       search_title = f"%{title}%"
       cursor.execute("""
SELECT *
       FROM books
       WHERE title Like ?
""",(search_title,))

       rows = cursor.fetchall()
       if not rows:
           print("No Book Found")
           conn.close()
       else:
           books =[]
           for row in rows:
               book_id,title,author,genre,availability = row
               book_object = Book.Book(book_id,title,author,genre,availability)
               books.append(book_object)
           conn.close()
           return books

   def search_by_author(self,author):
              conn = self.connect()
              cursor = conn.cursor()
              search_author = f"%{author}%"
              cursor.execute("""
       SELECT *
              FROM books
              WHERE author Like ?
       """,(search_author,)) 
              rows = cursor.fetchall()
              if not rows:
                  print("No Book Found")
                  conn.close()
              else:
                  books =[]
                  for row in rows:
                      book_id,title,author,genre,availability = row
                      book_object = Book.Book(book_id,title,author,genre,availability)
                      books.append(book_object)
                  conn.close()
                  return books

   def book_availability_checking(self,book_id):
       conn = self.connect()
       cursor = conn.cursor()
       cursor.execute("""
SELECT availability 
FROM books
WHERE book_id =?
       """,(book_id,))
       row = cursor.fetchone()

       if row[0] == 'Available':
           conn.close()
           return True
       else:
           row[0] == 'Borrowed'
           conn.close()
           return False
   def move_to_deleted_books(self,book_id):
       conn = self.connect()
       cursor = conn.cursor()
       cursor.execute("""
SELECT *FROM books
WHERE book_id =?
""",(book_id,))
       row = cursor.fetchone()

       if not row:
           conn.close()
           return False
       book_id,title,author,genre,availability = row

       cursor.execute("""
INSERT INTO deleted_books
(book_id,title,author,genre,availability)
VALUES(?,?,?,?,?)
""",(book_id,title,author,genre,availability))

       cursor.execute("""
DELETE FROM books
WHERE book_id =?
""",(book_id,))

       conn.commit()
       conn.close()
       return True

   def restore_deleted_books(self,book_id):
          conn = self.connect()
          cursor = conn.cursor()
          cursor.execute("""
   SELECT *FROM deleted_books
   WHERE book_id =?
   """,(book_id,))
          row = cursor.fetchone()
   
          if not row:
              conn.close()
              return False
          book_id,title,author,genre,availability = row
   
          cursor.execute("""
   INSERT INTO books
   (book_id,title,author,genre,availability)
   VALUES(?,?,?,?,?)
   """,(book_id,title,author,genre,availability))
   
          cursor.execute("""
   DELETE FROM deleted_books
   WHERE book_id =?
   """,(book_id,))
   
          conn.commit()
          conn.close()
          return True