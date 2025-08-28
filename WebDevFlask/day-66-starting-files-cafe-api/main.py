from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
import random
'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self) -> dict:
        return {column.name: getattr(self, column.name)for column in self.__table__.columns}



with app.app_context():
    db.create_all()
  

@app.route("/")
def home():
    return render_template("index.html")


#Get a random CAFE
@app.route("/random")
def random_cafe() -> dict:
    cafes = db.session.execute(db.select(Cafe)).scalars().all()
    random_cafe = random.choice(cafes)
    return jsonify(random_cafe.to_dict())

# HTTP GET - Read Record

@app.route("/all")
def all_cafes():
    all_cafes = db.session.execute(db.select(Cafe)).scalars().all()
    dict_all_cafes = [cafe.to_dict() for cafe in all_cafes]
    return jsonify(cafes=dict_all_cafes)

#HTTP search a record using location

@app.route("/search")
def search_cafe():
    location = request.args.get("loc")
    cafes_in_location = db.session.execute(db.select(Cafe).where(Cafe.location == location)).scalars().all()
    if len(cafes_in_location) == 0:
        message = {"Not Found": "Sorry we do not have a cafe in this location."}
        return jsonify(error=message)
    else:
        print(cafes_in_location)
        cafes_in_location = [cafe.to_dict() for cafe in cafes_in_location]
        return jsonify(cafes=cafes_in_location)
    
#=============================================== Helper function ====================================================================
def string_to_bool(request: str) -> bool:
    if request.lower() == "true":
        return True
    else:
        return False


# HTTP POST - Create Record
@app.route("/add", methods=["GET", "POST"])
def add_cafe():
    if request.method == "POST":
        cafe = Cafe(name=request.form["name"], map_url=request.form["map_url"], img_url=request.form["img_url"],
                    location=request.form["location"], seats=request.form["seats"], has_toilet=string_to_bool(request.form["has_toilet"]),
                    has_wifi=string_to_bool(request.form["has_wifi"]), has_sockets=string_to_bool(request.form["has_sockets"])
                    , can_take_calls=string_to_bool(request.form["can_take_calls"]),
                    coffee_price=request.form["coffee_price"])
        print(type(request.form["has_wifi"]))
        db.session.add(cafe)
        db.session.commit()
        message = {"success": "You have successfully added a new cafe."}
        return  jsonify(response=message)
    
# HTTP PUT/PATCH - Update Record

@app.route("/update-price", methods=["GET", "POST", "PATCH"])
def update_price():
    if request.method == "PATCH":
        cafe_id = request.args.get("id")
        new_price = request.args.get("price")

        try:
            cafe = db.session.execute(db.select(Cafe).where(Cafe.id == cafe_id)).scalar()
        except Exception:
            message = {"Not Found": "Sorry a cafe with that id was not found in the database."}
            return jsonify(error=message)
        else:
            cafe.coffee_price = new_price
            db.session.commit()
            return jsonify(success="Successfully updated the price.")            
# HTTP DELETE - Delete Record
@app.route("/report-closed", methods=["DELETE"])
def delete_cafe():
    key = request.args.get("api-key")
    cafe_id = request.args.get("id")
    cafe = db.session.execute(db.select(Cafe).where(Cafe.id == cafe_id)).scalar()
    print(key)

    if key != "TopSecretKey":
        return jsonify(error="Sorry, that is not allowed make sure you have the correct api key."), 403
    elif cafe:
        db.session.delete(cafe)
        db.session.commit()
        return jsonify(success="Successfully deleted the cafe from the database."), 200
    else:
        message = {"Not found": "Sorry could not find a cafe with this id in the database."}
        return jsonify(error=message), 404

if __name__ == '__main__':
    app.run(debug=True, port=5000, host="0.0.0.0")
