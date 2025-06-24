from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from dotenv import load_dotenv
import os
import requests

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

#Let us get Movie data through Movie search API

movie_api = os.getenv("API_KEY")
url = "https://api.themoviedb.org/3/authentication"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0NTM1MWY1OWU4MTA3MjIyYjgxODJkNTc0NGY0YTMzZSIsIm5iZiI6MTc1MDYxNTUzMC42NDcsInN1YiI6IjY4NTg0NWVhNjk1YWIxZTM0NDRiZDFjMSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.gHJGWPP7iIlEZpDnkD2s5CoVED4ooEUsTRy1uCueDyo"
}

response = requests.get(url, headers=headers)
print(response)

class EditForm(FlaskForm):
    rating = StringField('Your rating out of 10, eg 7.5', [DataRequired()])
    review = StringField('Your review', [DataRequired()])
    submit = SubmitField('submit')

class AddMovie(FlaskForm):
    movie_name = StringField("Movie Title", [DataRequired()])
    submit = SubmitField('submit')    

##CREATE DB
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


##CREATE TABLE
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String(250), nullable=True)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

with app.app_context():
    db.create_all()

## After adding the new_movie the code needs to be commented out/deleted.
## So you are not trying to add the same movie twice. The db will reject non-unique movie titles.


#     second_movie = Movie(
#         title="Avatar The Way of Water",
#         year=2022,
#         description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
#         rating=7.3,
#         ranking=9,
#         review="I liked the water.",
#         img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
#     )

# with app.app_context():
#     db.session.add(second_movie)
#     db.session.commit()

@app.route("/", methods=["GET", "POST"])
def home():
    all_movies = db.session.execute(db.select(Movie).order_by(Movie.id)).scalars() 
    return render_template("index.html", movies=all_movies)

@app.route("/add", methods=["POST", "GET"])
def add_movie():
    form = AddMovie()  
    return render_template("add.html", form=form)  

@app.route("/edit", methods=["POST", "GET"])
def edit_rating():
    form = EditForm()
    id = request.args.get('id', type=int)
    movie = db.get_or_404(Movie, id)
    if form.validate_on_submit():
        with app.app_context():
            movie = db.session.execute(db.select(Movie).where(Movie.id == id)).scalar()
            movie.rating = float(form.rating.data)
            movie.review = form.review.data
            db.session.commit()
            return redirect(url_for('home'))
    return render_template("edit.html", form=form)

@app.route("/delete")
def delete_movie():
    movie_id = request.args.get("id")
    movie = db.get_or_404(Movie, movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for("home"))

if __name__ == '__main__':
    app.run(debug=True, port=3000)