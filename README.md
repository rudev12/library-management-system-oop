# Library Management System

A simple Object-Oriented Library Management System built using Python.

This project demonstrates the practical use of:

* Object-Oriented Programming (OOP)
* Classes and Objects
* Dictionaries
* File Handling
* Data Persistence
* Searching and Filtering

---

## Features

### Library Features

* Add new books
* Prevent duplicate book IDs
* Search books by ID
* Remove books
* Display all books
* Check book availability
* Library statistics
* Count books by author
* Search books by title
* Search books by author
* Partial title search

### Book Features

* Borrow books
* Return books
* Update book title
* Display book details

### File Handling Features

* Save books permanently in `library_data.txt`
* Load books automatically when the program starts
* Prevent duplicate entries after restarting the program
* Handle missing file errors

---

## Technologies Used

* Python 3
* Object-Oriented Programming
* File Handling
* Dictionaries

---

## Project Structure

```text
Library-Management-System/
│
├── main.py
├── library_data.txt
└── README.md
```

---

## Classes

### Library Class

Methods:

* `add_book()`
* `remove_book()`
* `search_book()`
* `show_all_books()`
* `library_stats()`
* `search_by_title()`
* `search_by_author()`
* `search_partial_title()`
* `count_book_by_author()`
* `check_availability()`
* `load_books()`

---

### Book Class

Methods:

* `show_book()`
* `borrow_book()`
* `return_book()`
* `update_title()`

---

## File Storage

Books are stored in:

```text
library_data.txt
```

Format:

```text
101,Python Basics,Rudhraksh
102,C++ Basics,Swayam
```

Each line represents one book.

---

## How to Run

1. Clone the repository.

```bash
git clone <repository-link>
```

2. Open the project in VS Code.

3. Run:

```bash
python main.py
```

---

## Current Concepts Used

* Classes and Objects
* Constructors
* Methods
* Dictionaries
* Loops
* Conditionals
* File Handling
* Exception Handling
* Data Persistence

---

## Future Improvements

* Menu-driven interface
* Save borrowed status in file
* Delete book data from file
* Update book data in file
* User login system
* GUI using Tkinter
* Database integration using SQLite

---

## Author

**Rudhraksh Shukla**

Python Learning Project – Library Management System
