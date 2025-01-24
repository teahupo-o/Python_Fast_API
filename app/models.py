from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from . import database


class Author(database.Base):
    __tablename__ = "author"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    surname = Column(String(100), nullable=False)
    date_of_birth = Column(Integer, nullable=False)

class Book(database.Base):
    __tablename__ = "book"

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    isbn = Column(String(250), nullable=False)
    author_id = Column(ForeignKey("author.id"))
    author = relationship("Author", backref="books")

class User(database.Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    user_name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)

class Loan(database.Base):
    __tablename__ = "loan"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    book_id = Column(Integer, ForeignKey('book.id'))
    date_of_loan = Column(Integer, nullable=False)
    date_of_return = Column(Integer, nullable=False)