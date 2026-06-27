# Library Management System

A console-based Library Management System developed using Python and Object-Oriented Programming (OOP). This project allows users to manage books, search books, borrow and return books, and maintain library records using file handling.

---

## Project Features

### Book Management

* Add new books
* Remove existing books
* Update book titles
* Display book information

### Search System

* Search books by title
* Search books by author
* Partial title search
* Partial author search
* Display total matching books

### Borrow and Return System

* Borrow books
* Return books
* Check book availability
* Prevent borrowing unavailable books

### File Handling

* Save library data automatically
* Load books from file during startup
* Maintain book availability status

### Library Statistics

* Total books
* Available books
* Borrowed books

### Menu Driven System

* Add Book
* Remove Book
* Search By Title
* Search By Author
* Borrow Book
* Return Book
* Show All Books
* Library Statistics
* Exit

---

## Technologies Used

* Python 3
* Object-Oriented Programming
* File Handling
* Exception Handling
* Dictionary Data Structure

---

## Project Structure

```text
Library Management System
│
├── Book Class
├── Library Class
├── Menu System
└── library_data.txt
```

---

## Classes

### Book Class

Responsible for:

* Book ID
* Title
* Author
* Availability Status

Methods:

* show_book()
* update_title()

---

### Library Class

Responsible for:

* Managing books
* Searching books
* Borrowing books
* Returning books
* Saving data
* Loading data
* Library statistics

Methods:

* add_book()
* remove_book()
* search_book()
* search_by_title()
* search_by_author()
* borrow_book()
* return_book()
* show_all_books()
* library_stats()
* save_book()
* load_book()

---

## Data Storage

Books are stored in:

```text
library_data.txt
```

Format:

```text
101,Python Basics,Rudhraksh,True
102,C++ Basics,Swayam,False
```

Where:

* True = Available
* False = Borrowed

---

## How to Run

1. Install Python 3.
2. Download the project files.
3. Open the terminal.
4. Run:

```bash
python main.py
```

---

## Concepts Used

* Classes and Objects
* Encapsulation
* Dictionaries
* Loops
* Conditional Statements
* Exception Handling
* File Handling
* Object-Oriented Programming
* Menu Driven Programs

---

## Future Improvements

* Employee Management
* Book Issue History
* Automatic Book IDs
* Fine Calculation System
* User Accounts
* GUI Version using Tkinter
* Database Integration using SQLite

---

## Author

Rudhraksh Shukla

Library Management System using Python and Object-Oriented Programming.
