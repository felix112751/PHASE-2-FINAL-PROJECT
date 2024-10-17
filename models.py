from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Model for Artists
class Artist(db.Model):
    __tablename__ = 'artists'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    artworks = db.relationship('Artwork', backref='artist', lazy=True)

# Model for Artworks
class Artwork(db.Model):
    __tablename__ = 'artworks'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    image = db.Column(db.String(500), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    detail = db.Column(db.Text, nullable=True)
    likes = db.Column(db.Integer, default=0)
    sold = db.Column(db.Boolean, default=False)

    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'), nullable=False)

# Model for Cart
class Cart(db.Model):
    __tablename__ = 'carts'

    id = db.Column(db.Integer, primary_key=True)
    artwork_id = db.Column(db.Integer, db.ForeignKey('artworks.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    # Additional attribute for the Cart
    quantity = db.Column(db.Integer, nullable=False, default=1)

    artwork = db.relationship('Artwork', backref='carts', lazy=True)
