from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db, Artist, Artwork, User, Cart

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///art_app.db'  # Change this as needed
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

migrate = Migrate(app, db)

# Route to get all artists
@app.route('/artists', methods=['GET'])
def get_artists():
    artists = Artist.query.all()
    return jsonify([{'id': artist.id, 'name': artist.name} for artist in artists])

# Route to get all artworks
@app.route('/artworks', methods=['GET'])
def get_artworks():
    artworks = Artwork.query.all()
    return jsonify([{
        'id': artwork.id,
        'title': artwork.title,
        'image': artwork.image,
        'year': artwork.year,
        'price': artwork.price,
        'detail': artwork.detail,
        'likes': artwork.likes,
        'sold': artwork.sold,
        'artist_id': artwork.artist_id
    } for artwork in artworks])

# Route to create a new artist
@app.route('/artists', methods=['POST'])
def create_artist():
    data = request.json
    new_artist = Artist(name=data['name'])
    db.session.add(new_artist)
    db.session.commit()
    return jsonify({'id': new_artist.id, 'name': new_artist.name}), 201

# Route to create a new artwork
@app.route('/artworks', methods=['POST'])
def create_artwork():
    data = request.json
    new_artwork = Artwork(
        title=data['title'],
        image=data['image'],
        year=data['year'],
        price=data['price'],
        detail=data.get('detail', ''),
        artist_id=data['artist_id']
    )
    db.session.add(new_artwork)
    db.session.commit()
    return jsonify({'id': new_artwork.id, 'title': new_artwork.title}), 201

# Route to create a new user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    new_user = User(username=data['username'], password=data['password'], email=data['email'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'id': new_user.id, 'username': new_user.username}), 201

# Route to get user's cart
@app.route('/users/<int:user_id>/cart', methods=['GET'])
def get_user_cart(user_id):
    carts = Cart.query.filter_by(user_id=user_id).all()
    return jsonify([{'id': cart.id, 'artwork_id': cart.artwork_id, 'quantity': cart.quantity} for cart in carts])

if __name__ == '__main__':
    app.run(debug=True)
