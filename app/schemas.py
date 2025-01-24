from pydantic import BaseModel

class NewBook(BaseModel):
    name: str
    isbn: str
    author_id: int

class NewBookLoan(BaseModel):
    user_id: int
    book_id: int
    date_of_loan : int
    date_of_return : int

class NewAuthor(BaseModel):
    name: str
    surname : str
    date_of_birth : int

class NewUser(BaseModel):
    user_name: str
    email: str