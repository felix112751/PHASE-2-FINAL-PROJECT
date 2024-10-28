from flask import Flask, make_response, request, jsonify
from flask_migrate import Migrate
from models import db, User, Post, Artwork, Artist
from flask_cors import CORS

app = Flask(__name__)
migrate = Migrate(app, db)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///flask.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)

db.init_app(app)

@app.route('/')
def index():
    return 'Welcome to flask'

@app.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'GET':
        response = [user.to_dict() for user in User.query.all()]
        return make_response(response, 200)

    if request.method == 'POST':
        data = request.get_json()
        new_user = User(username=data['username'], email=data['email'])
        db.session.add(new_user)
        db.session.commit()
        return make_response(new_user.to_dict(), 201)

@app.route('/posts', methods=['GET', 'POST'])
def posts():
    if request.method == 'GET':
        response = [post.to_dict() for post in Post.query.all()]
        return make_response(response, 200)

from flask import jsonify, request, make_response

@app.route('/artworks', methods=['GET', 'POST'])
def artworks():
    if request.method == 'GET':
        response = [artwork.to_dict() for artwork in Artwork.query.all()]
        return make_response(jsonify(response), 200)

    if request.method == 'POST':
        data = request.get_json()
        if not data:
            return make_response(jsonify({"error": "Invalid JSON payload"}), 400)

        try:
            new_artwork = Artwork(
                title=data['title'],
                price=data['price'],
                year=data['year'],
                detail=data['detail'],
                sold=data['sold'],
                likes=data['likes'],
                image=data['image'],
                artist_id=data['artist_id']
            )
            db.session.add(new_artwork)
            db.session.commit()
            return make_response(jsonify(new_artwork.to_dict()), 201)

        except KeyError as e:
            return make_response(jsonify({"error": f"Missing key: {e}"}), 400)





@app.route('/artworks/<int:id>', methods=['PUT', 'DELETE'])
def artwork_detail(id):
    artwork = Artwork.query.get_or_404(id)

    if request.method == 'PUT':
        data = request.get_json()
        artwork.title = data['title']
        artwork.description = data['description']
        artwork.artist_id = data['artist_id']
        db.session.commit()
        return make_response(artwork.to_dict(), 200)

    if request.method == 'DELETE':
        db.session.delete(artwork)
        db.session.commit()
        return make_response('', 204)

@app.route('/artists', methods=['GET', 'POST'])
def artists():
    if request.method == 'GET':
        response = [artist.to_dict() for artist in Artist.query.all()]
        return make_response(response, 200)

    if request.method == 'POST':
        data = request.get_json()
        new_artist = Artist(name=data['name'])
        db.session.add(new_artist)
        db.session.commit()
        return make_response(new_artist.to_dict(), 201)

@app.route('/artists/<int:id>', methods=['PUT', 'DELETE'])
def artist_detail(id):
    artist = Artist.query.get_or_404(id)

    if request.method == 'PUT':
        data = request.get_json()
        artist.name = data['name']
        db.session.commit()
        return make_response(artist.to_dict(), 200)

    if request.method == 'DELETE':
        db.session.delete(artist)
        db.session.commit()
        return make_response('', 204)

if __name__ == '__main__':
    app.run(port=4000, debug=True)