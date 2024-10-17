from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db, Artist, Artwork, Cart


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flask.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'mysecretkey'

db.init_app(app)
migrate = Migrate(app, db)



@app.route('/')
def index():
    return 'Welcome to the virtual art gallery'

@app.route('/artists')
def artists():
    return 'List of artists'


@app.route('/artworks')
def artworks():
    return 'List of artworks'

@app.route('/cart')
def cart():
    return 'List of artworks'


if __name__ == '__main__':
    app.run(port =  4000, debug = True)  # run the app in debug mode on port 500