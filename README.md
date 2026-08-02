# Library Management System

A console-based Library Management System developed in Python using Object-Oriented Programming and SQLite. The project manages books, borrowing and returning operations, searching, deletion and restoration of books, and role-based access through Admin and Front Desk login systems.

## Features

### Authentication and Role-Based Access

The system provides two types of users:

* **Admin**

  * Add new books
  * Remove books
  * Search books by title
  * Search books by author
  * Borrow books
  * Return books
  * View all books
  * Restore deleted books

* **Front Desk**

  * Search books by title
  * Search books by author
  * Borrow books
  * Return books
  * View all books

After successful authentication, the user is directed to the appropriate console based on their role.

## Demo Login Credentials

The current version of the project uses hardcoded credentials for demonstration and testing purposes.

### Admin Login

```text
Username: adminrudev12
Password: rudev12
```

### Front Desk Login

```text
Username: deskrudev12
Password: rudev123
```

These credentials are provided so users can test the application after cloning the repository.

**Note:** The current authentication system is intended for learning and demonstration purposes and is not suitable for production use.

## Book Management

The system allows the Admin to:

* Add books with title, author, and genre
* Prevent duplicate books based on title and author
* Remove books from the active book database
* Move deleted books to a separate deleted-books table
* Restore previously deleted books

Each book contains:

* Book ID
* Title
* Author
* Genre
* Availability status

## Search Functionality

Books can be searched using:

* Title
* Author

The search supports partial text matching, allowing users to find books without entering the complete title or author name.

## Borrow and Return System

The system maintains book availability using two states:

* `Available`
* `Borrowed`

Before borrowing a book, the system checks:

1. Whether the Book ID exists
2. Whether the book is already borrowed

Before returning a book, the system checks:

1. Whether the Book ID exists
2. Whether the book is already available

This prevents invalid borrowing and returning operations.

## Delete and Restore System

Instead of permanently deleting a book immediately, the system moves the book from the `books` table to the `deleted_books` table.

The deletion flow is:

```text
books
  |
  | Delete
  v
deleted_books
```

The restoration flow is:

```text
deleted_books
  |
  | Restore
  v
books
```

This allows deleted books to be restored later.

## Project Structure

```text
Library project/
│
├── main.py
├── login.py
├── admin_console.py
├── desk_console.py
├── library.py
├── database.py
├── book.py
├── README.md
└── .gitignore
```

The SQLite database file is not included in the repository. It is created locally when the application initializes the required database tables.

### `main.py`

Acts as the entry point of the application.

It:

* Starts the login process
* Receives the authenticated user's role
* Opens the Admin console for Admin users
* Opens the Front Desk console for Front Desk users

### `login.py`

Handles user authentication and role selection.

It currently supports:

* Admin login
* Front Desk login

The login system returns the authenticated user's role to `main.py`.

### `admin_console.py`

Provides the Admin interface with access to the administrative and library management operations currently implemented in the project.

### `desk_console.py`

Provides a restricted interface for Front Desk users.

Front Desk users can search, borrow, return, and view books but do not have access to administrative operations such as adding, deleting, or restoring books.

### `library.py`

Contains the main library business logic.

It manages operations such as:

* Adding books
* Searching books
* Borrowing books
* Returning books
* Removing books
* Restoring deleted books
* Checking book availability
* Displaying books

The class communicates with the database layer to perform persistent data operations.

### `database.py`

Handles SQLite database operations.

It contains functionality for:

* Creating database tables
* Inserting books
* Fetching books
* Updating book availability
* Updating book titles
* Checking Book IDs
* Checking duplicate books
* Searching books
* Moving books to the deleted-books table
* Restoring deleted books

The database layer is responsible for interacting with SQLite, while the Library class handles the higher-level business logic.

### `book.py`

Contains the `Book` class, which represents a book object and stores:

* Book ID
* Title
* Author
* Genre
* Availability

It also provides functionality for displaying book information.

## Database

The project uses SQLite as its database system.

The application uses two main tables:

### `books`

Stores active library books.

```text
book_id
title
author
genre
availability
```

### `deleted_books`

Stores books that have been removed from the active library.

```text
book_id
title
author
genre
availability
```

The `book_id` is used to identify books and maintain their records between the active and deleted-book tables.

## Technologies Used

* Python
* Object-Oriented Programming
* SQLite
* SQL
* Python `sqlite3` module

## How to Run

### 1. Clone the repository

```bash
git clone <your-repository-url>
```

### 2. Open the project directory

```bash
cd Library-project
```

### 3. Run the application

```bash
python main.py
```

### 4. Database Setup

The SQLite database file is not included in the GitHub repository.

When the application is initialized, the required database tables are created locally.

No pre-existing `library.db` file is required to run the project.

### 5. Select a Login Type

Choose one of the available options:

```text
1. Login As Admin
2. Login As Front Desk
```

Use the demo credentials provided above to access the corresponding console.

## Application Architecture

The application follows a modular structure that separates authentication, user interfaces, library business logic, and database operations.

```text
                    User
                      |
                      v
                  main.py
                      |
                      v
                  login.py
                      |
                      v
              Authentication
                      |
              +-------+-------+
              |               |
              v               v
            Admin         Front Desk
              |               |
              v               v
      admin_console.py   desk_console.py
              |               |
              +-------+-------+
                      |
                      v
                  library.py
                      |
                      v
                 database.py
                      |
                      v
                   SQLite
```

The project is being developed incrementally, with the goal of maintaining a clear separation between business logic and database operations.

## Future Development

The following features and improvements are planned for future versions of the project:

* Complete migration of remaining library features to SQLite
* Implement Library Statistics using SQLite queries
* Replace hardcoded login credentials with a SQLite-based user management system
* Support multiple user accounts
* Store user roles in the database
* Improve role-based access control
* Implement secure password handling
* Add forgot-password and password-reset functionality
* Improve database validation and error handling
* Add automated testing
* Further refactor and improve the project architecture as the system grows

## Project Status

The project is currently under active development.

The core library management functionality, SQLite database integration, book borrowing and returning, book deletion and restoration, and role-based login system are currently implemented.

Additional features and improvements will be added in future versions as the project continues to evolve.

## Purpose

This project was developed as a practical learning project to strengthen understanding of:

* Python Object-Oriented Programming
* Modular code organization
* Separation of business logic and database operations
* SQLite database integration
* SQL query handling
* Authentication
* Role-based access
* Debugging and error handling
* Software architecture

The project is being developed incrementally to apply programming concepts in a practical application rather than as a single completed system.
