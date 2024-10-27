from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

# Association table for user groups
user_groups = db.Table('user_groups',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('group_id', db.Integer, db.ForeignKey('groups.id'), primary_key=True)
)

class Artist(db.Model, SerializerMixin):
    __tablename__ = 'artists'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

    artworks = db.relationship('Artwork', back_populates="artist")

    def __repr__(self):
        return f'<Artist {self.name}>'

class Artwork(db.Model, SerializerMixin):
    __tablename__ = 'artworks'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    image = db.Column(db.String(255))  # Image field
    year = db.Column(db.Integer)  # Year field
    price = db.Column(db.Float)  # Price field
    detail = db.Column(db.String(255))  # Detail field
    likes = db.Column(db.Integer, default=0)  # Likes field
    sold = db.Column(db.Boolean, default=False)  # Sold field
    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'))  # Reference to 'artists'
    artist = db.relationship('Artist', back_populates="artworks")

    serialize_rules = ('-artist.artworks',)

    def __repr__(self):
        return f'<Artwork {self.title}>'

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)  # Password field

    posts = db.relationship('Post', back_populates="user")
    groups = db.relationship('Group', secondary=user_groups, back_populates="users")
    cart_items = db.relationship('Cart', back_populates="user")

    serialize_rules = ('-posts.user', '-groups.users',)

    @validates('email')
    def validate_email(self, key, address):
        if '@' not in address:
            raise ValueError("failed simple email validation")
        return address

class Post(db.Model, SerializerMixin):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    content = db.Column(db.String(120), nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))  # Reference to 'users'
    user = db.relationship('User', back_populates="posts")

    serialize_rules = ('-user.groups',)

    def __repr__(self):
        return f'<Post {self.title}>'

class Group(db.Model, SerializerMixin):
    __tablename__ = 'groups'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

    users = db.relationship('User', secondary=user_groups, back_populates="groups")

    def __repr__(self):
        return f'<Group {self.name}>'

class Cart(db.Model, SerializerMixin):
    __tablename__ = 'carts'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))  # Reference to 'users'
    user = db.relationship('User', back_populates="cart_items")

    # Add fields for cart items if needed

    def __repr__(self):
        return f'<Cart {self.id}>'