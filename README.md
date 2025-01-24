
# Library Management API

This project is a REST API built with FastAPI for managing a library system. It supports CRUD operations for books, authors, users, and book loans, using SQLite as the database. The project also includes features like data validation with Pydantic and database migrations with Alembic.

---

## Features
- Manage books, authors, users, and loans.
- Simple SQLite database setup.
- Validations using Pydantic.
- Alembic for database migrations.
- FastAPI and Uvicorn for an efficient server framework.

---

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-repo/library-api.git
   cd library-api
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Start the server:
   ```bash
   uvicorn main:app --reload
   ```

4. Access the API at `http://127.0.0.1:8000`.

---

## Endpoints

### 1. GET /all_books
- **Description**: Returns a list of all books, including their authors.
- **Response Example**:
  ```json
  {
    "books": [
      {
        "id": 1,
        "name": "Book Title",
        "isbn": "123-4567890123",
        "author_id": 1,
        "author_name": "Author First Name",
        "author_surname": "Author Last Name",
        "date_of_birth": "1970"
      }
    ]
  }
  ```

### 2. POST /books
- **Description**: Creates a new book.
- **Request Example**:
  ```json
  {
    "name": "Book Title",
    "isbn": "123-4567890123",
    "author_id": 1
  }
  ```
- **Response**: Status `201 Created`.

### 3. GET /all_authors
- **Description**: Returns a list of all authors.
- **Response Example**:
  ```json
  {
    "author": [
      {
        "id": 1,
        "name": "Author First Name",
        "surname": "Author Last Name",
        "date_of_birth": "1970-01-01"
      }
    ]
  }
  ```

### 4. POST /book_loan
- **Description**: Creates a new book loan (a user borrows a book).
- **Request Example**:
  ```json
  {
    "user_id": 1,
    "book_id": 1,
    "date_of_loan": 20230101,
    "date_of_return": 20230115
  }
  ```
- **Response**: Status `201 Created`.

### 5. POST /author
- **Description**: Adds a new author.
- **Request Example**:
  ```json
  {
    "name": "Author First Name",
    "surname": "Author Last Name",
    "date_of_birth": 1970
  }
  ```
- **Response**: Status `201 Created`.

### 6. POST /user
- **Description**: Adds a new user.
- **Request Example**:
  ```json
  {
    "user_name": "User Name",
    "email": "user@example.com"
  }
  ```
- **Response**: Status `201 Created`.

---

## Testing the API

- Use a tool like **Postman** to test the endpoints.
- Ensure the correct request formats (as described above) are used for POST requests.
- Verify responses for successful operation.

---

## Technologies Used

- **Framework**: FastAPI  
- **Database**: SQLite  
- **ORM**: SQLAlchemy  
- **Validation**: Pydantic  
- **Migrations**: Alembic  
- **Server**: Uvicorn  

---


