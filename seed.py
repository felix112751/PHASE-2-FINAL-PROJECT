from app import app
from models import db, Artist, Artwork, Cart, User
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///art.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'mysecretkey'
db.init_app(app)

with app.app_context():
    db.create_all()

    # Create artists
    artist1 = Artist(name='Vincent van Gogh')
    artist2 = Artist(name='Pablo Picasso')
    artist3 = Artist(name='Leonardo da Vinci')
    artist4 = Artist(name='Edvard Munch')
    artist5 = Artist(name='Johannes Vermeer')
    artist6 = Artist(name='Salvador Dali')
    artist7 = Artist(name='Rembrandt')
    artist8 = Artist(name='Sandro Botticelli')
    artist9 = Artist(name='Grant Wood')
    artist10 = Artist(name='Gustav Klimt')

    # Add artists to the session
    db.session.add_all([artist1, artist2, artist3, artist4, artist5, artist6, artist7, artist8, artist9, artist10])
    db.session.commit()

    # Create artworks
    artwork1 = Artwork(
        title="Starry Night",
        image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQoiXokZHJc3iND6Uqax-iQ-nU6PmC5lRPqIw&s",
        year=1889,
        price=5000,
        detail="Starry Night is one of Vincent van Gogh's most iconic paintings, created in 1889. It depicts a swirling night sky over a tranquil village, with bold, expressive brushstrokes capturing the motion of the stars and the moon. The scene is framed by a dark cypress tree in the foreground, contrasting against the vibrant, star-filled sky.",
        likes=8,
        sold=False,
        artist_id=artist1.id
    )

    artwork2 = Artwork(
        title="Mona Lisa",
        image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ0s5B5TIgNtd8NBG31BBu2v1cCxIZi3AEE2g&s",
        year=1503,
        price=100000,
        detail="The Mona Lisa is a portrait painting by Leonardo da Vinci, completed between 1503 and 1506. The artwork depicts a woman with an enigmatic expression, famously known for her subtle smile.",
        likes=10,
        sold=False,
        artist_id=artist3.id
    )

    artwork3 = Artwork(
        title="The Persistence of Memory",
        image="https://cdn.britannica.com/96/240496-138-66D89FAD/Salvador-Dali-Persistence-of-Memory.jpg?w=800&h=450&c=crop",
        year=1931,
        price=20000,
        detail="The painting presents a dream-like landscape where time appears to dissolve. Soft, melting clocks drape over tree branches, suggesting the malleability and subjective nature of time.",
        likes=8,
        sold=False,
        artist_id=artist6.id
    )

    artwork4 = Artwork(
        title="The Scream",
        image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS1kStiFO1k0-RIzz6I4MAXcPt1C4sdYSvV7A&s",
        year=1893,
        price=60000,
        detail="The Scream by Edvard Munch is a renowned expressionist painting created in 1893. The artwork depicts a figure on a bridge against a turbulent sky, with its mouth open in a scream of existential anguish.",
        likes=8,
        sold=False,
        artist_id=artist4.id
    )

    artwork5 = Artwork(
        title="Girl with a Pearl Earring",
        image="https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/1665_Girl_with_a_Pearl_Earring.jpg/800px-1665_Girl_with_a_Pearl_Earring.jpg",
        year=1665,
        price=80000,
        detail="Girl with a Pearl Earring by Johannes Vermeer is often referred to as the Mona Lisa of the North. It features a young girl wearing an exotic turban and an exceptionally large pearl earring.",
        likes=9,
        sold=False,
        artist_id=artist5.id
    )

    artwork6 = Artwork(
        title="Guernica",
        image="https://upload.wikimedia.org/wikipedia/en/thumb/7/74/PicassoGuernica.jpg/400px-PicassoGuernica.jpg",
        year=1937,
        price=30000,
        detail="Guernica is a renowned mural painting by Pablo Picasso, created in response to the bombing of Guernica during the Spanish Civil War. It is known for its powerful depiction of the horrors of war.",
        likes=12,
        sold=False,
        artist_id=artist2.id
    )

    artwork7 = Artwork(
        title="The Night Watch",
        image="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/The_Night_Watch_-_HD.jpg/1200px-The_Night_Watch_-_HD.jpg",
        year=1642,
        price=20002,
        detail="The Night Watch by Rembrandt van Rijn, completed in 1642, depicts a dynamic scene of a militia company, led by Captain Frans Banning Cocq and his lieutenant.",
        likes=6,
        sold=False,
        artist_id=artist7.id
    )

    artwork8 = Artwork(
        title="The Birth of Venus",
        image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR9v3SJUhLh65lLuJo-3nsm4cPguDQb_4mGyg&s",
        year=1486,
        price=400000,
        detail="The Birth of Venus is a renowned painting by Sandro Botticelli, depicting the mythological birth of Venus emerging from the sea on a shell.",
        likes=13,
        sold=False,
        artist_id=artist8.id
    )

    artwork9 = Artwork(
        title="American Gothic",
        image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRjVnMwqihzhYhxYeyEr6qvyGlD_mbAz3NK7Q&s",
        year=1930,
        price=34000,
        detail="American Gothic is a famous painting by Grant Wood, portraying a stern-looking man and woman standing in front of a traditional American farmhouse.",
        likes=4,
        sold=False,
        artist_id=artist9.id
    )

    artwork10 = Artwork(
        title="The Kiss",
        image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS87titbSUj74DnfP14bZn4stGqggtO8C2vjw&s",
        year=1908,
        price=10000,
        detail="The Kiss by Gustav Klimt is considered one of his masterpieces, known for its use of gold leaf and intricate patterns symbolizing romantic love.",
        likes=13,
        sold=False,
        artist_id=artist10.id
    )

    # Add the artworks to the session
    db.session.add_all([artwork1, artwork2, artwork3, artwork4, artwork5, artwork6, artwork7, artwork8, artwork9, artwork10])
    db.session.commit()

     # Create users
    user1 = User(username='artlover1', password='password123', email='artlover1@example.com')
    user2 = User(username='galleryfan', password='password456', email='galleryfan@example.com')
    user3 = User(username='artcollector', password='password789', email='artcollector@example.com')

    # Add users to the session
    db.session.add_all([user1, user2, user3])
    db.session.commit()

    # Add some carts
    cart1 = Cart(artwork_id=artwork1.id, user_id=user1.id, quantity=1)
    cart2 = Cart(artwork_id=artwork2.id, user_id=user1.id, quantity=2)
    cart3 = Cart(artwork_id=artwork1.id, user_id=user2.id, quantity=1)

    db.session.add_all([cart1, cart2, cart3])
    db.session.commit()

    print("Database seeded successfully!")

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        print("Seeding data...")