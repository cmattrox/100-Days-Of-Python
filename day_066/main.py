import random
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy()
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

with app.app_context():
    db.create_all()    


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/random", methods=["GET"])
def random_cafe():
    res = db.session.execute(db.select(Cafe))
    all_cafes = res.scalars().all()
    random_cafe = random.choice(all_cafes)

    return jsonify(random_cafe.to_dict())

@app.route("/all", methods=["GET"])
def all_cafes():
    res = db.session.execute(db.select(Cafe))
    all_cafes = res.scalars().all()

    return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])

@app.route("/search", methods=["GET"])
def search():
    loc = request.args.get("loc")
    res = db.session.execute(db.select(Cafe).where(Cafe.location == loc))
    cafes = res.scalars().all()

    if cafes:
        return jsonify(cafes=[cafe.to_dict() for cafe in cafes])
    else:
        return jsonify({"error": {"Not Found": "Sorry, we don't have a cafe at that location"}})

# HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def add():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("map_url"),
        location=request.form.get('location'),
        has_sockets=bool(request.form.get('has_sockets')),
        has_wifi=bool(request.form.get('has_wifi')),
        has_toilet=bool(request.form.get('has_toilet')),
        can_take_calls=bool(request.form.get('can_take_calls')),
        seats=request.form.get('seats'),
        coffee_price=request.form.get('coffee_price'),
    )

    db.session.add(new_cafe)
    db.session.commit()

    return jsonify(response={"success": "Successfully added the new cafe"})

# HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int: id>")
def update_price(id):
    cafe = db.get_or_404(Cafe, id)
    new_price = request.args.get('new-price')
    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify({"success": "Successfully updated the price"})
    else:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database"})

# HTTP DELETE - Delete Record
@app.route("/report-closed/<int: id>")
def report_closed(id):
    api_key = request.args.get("api-key")
    if api_key == "TopSecretAPIKey":
        cafe = db.get_or_404(Cafe, id)
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            
            return jsonify({"Success": "Cafe was successfully removed from the database"})
        else:
            return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database"})
    else:
        return jsonify({"error": "Sorry, that's not allowed. Make sure you have the correct API key"})

if __name__ == '__main__':
    app.run(debug=True)
