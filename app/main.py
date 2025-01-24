from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from starlette import status
from typing import Annotated
from app import schemas

from . import models
from . import database

app = FastAPI()
database.Base.metadata.create_all(database.engine)

def get_db():
    db = database.SessionLocal()

    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


@app.get("/")
def app_running():
    return {"message": "The app is running!"}


@app.get("/all_books", status_code=status.HTTP_200_OK)
async def get_all_books(db: db_dependency):
    books = db.query(models.Book).join(models.Author, models.Author.id == models.Book.author_id).all()
    for book in books:
        book = {
            "id": book.id,
            "name": book.name,
            "isbn": book.isbn,
            "author_id": book.author_id,
            "author_name": book.author.name,
            "author_surname": book.author.surname,
            "date_of_birth": book.author.date_of_birth,
        }
    return {"books": books}


@app.get("/all_authors", status_code=status.HTTP_200_OK)
async def get_all_author(db: db_dependency):
    authors = db.query(models.Author).all()
    return {"author": authors}


@app.post("/book", status_code=status.HTTP_201_CREATED)
async def add_book(db: db_dependency, book_request: schemas.NewBook):
    new_book = models.Book(**book_request.model_dump())
    db.add(new_book)
    db.commit()


@app.post("/book_loan", status_code=status.HTTP_201_CREATED)
async def add_loan(db: db_dependency, book_loan_request: schemas.NewBookLoan):
    new_book_loan = models.Loan(**book_loan_request.model_dump())
    db.add(new_book_loan)
    db.commit()


@app.post("/author", status_code=status.HTTP_201_CREATED)
async def add_author(db: db_dependency, author_request: schemas.NewAuthor):
    new_author = models.Author(**author_request.model_dump())
    db.add(new_author)
    db.commit()


@app.post("/user", status_code=status.HTTP_201_CREATED)
async def add_user(db: db_dependency, user_request: schemas.NewUser):
    new_user = models.User(**user_request.model_dump())
    db.add(new_user)
    db.commit()

