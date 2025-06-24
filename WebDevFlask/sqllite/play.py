# import sqlite3

# db = sqlite3.connect("books_collection.db")
# cursor = db.cursor()

# #Let us perform some action in the database
# # cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")

# cursor.execute("INSERT INTO books VALUES(1, 'Universe Book', 'Magobo Lesaomako', '7.6')")
# db.commit()

from flask import Flask
from flask import request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, Float, String

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

#Let us create the flask app
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
db.init_app(app)

class Books(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(unique=True)
    author: Mapped[str]
    rating: Mapped[float]
  

with app.app_context():
    db.create_all()
    book1 = Books(
            id = 1,
            title = "Harry Porter",
            author = "Magobo Lesaomako",
            rating = 7.9
        )
    db.session.add(book1)
    db.session.commit()  




