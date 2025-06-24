from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column 
from sqlalchemy.orm import DeclarativeBase

#Let us create a class to use for model object
class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

#Let us create a model class now
class Book(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(unique=True)
    author: Mapped[str] 
    review: Mapped[float]

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
db.init_app(app)    

all_books = []

with app.app_context():
    db.create_all()
    db.session.close()

@app.route('/')
def home():
    with app.app_context():
        all_books = (db.session.execute(db.select(Book).order_by(Book.id)).scalars()).all()
    return render_template('index.html', length=len(all_books), books=all_books)


@app.route("/add", methods=["POST", "GET"])
def add():
    if request.method == "POST":
        book = Book(
            title = request.form.get("name"),
            author = request.form.get("author"),
            review = request.form.get("rating")
        )

        with app.app_context():
            db.session.add(book)
            db.session.commit()
        return redirect(url_for("home"))
    
    return render_template('add.html')

@app.route("/edit", methods=["POST", "GET"])
def edit():
    id = request.args.get("id", type=int)
    with app.app_context():
        book = db.session.execute(db.select(Book).where(Book.id == id)).scalar()
        db.session.close()

    if request.method == "POST":
        with app.app_context():
            book = db.session.execute(db.select(Book).where(Book.id == id)).scalar()
            book.review = request.form.get("review")
            db.session.commit()
            db.session.close()
        return redirect(url_for("home"))
    return render_template("edit.html", book=book)

@app.route("/delete")
def delete_item():
    book_id = request.args.get('id')

    book = db.get_or_404(Book, book_id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True, port=3000)

