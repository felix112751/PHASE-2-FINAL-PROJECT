from app import app, db
from models import User, Post, Group, Artwork, Artist, Cart

with app.app_context():
    db.drop_all()
    db.create_all()

    # Clear existing data
    db.session.query(User).delete()
    db.session.query(Post).delete()
    db.session.query(Group).delete()
    db.session.query(Artwork).delete()
    db.session.query(Artist).delete()
    db.session.commit()

    # Create artists
    artists = [
        Artist(name='Vincent van Gogh'),
        Artist(name='Pablo Picasso'),
        Artist(name='Leonardo da Vinci'),
        Artist(name='Edvard Munch'),
        Artist(name='Johannes Vermeer'),
        Artist(name='Salvador Dali'),
        Artist(name='Rembrandt'),
        Artist(name='Sandro Botticelli'),
        Artist(name='Grant Wood'),
        Artist(name='Gustav Klimt'),
    ]
    db.session.add_all(artists)
    db.session.commit()

    # Create artworks
    artworks = [
        Artwork(title="Starry Night", image="...", year=1889, price=5000, detail="...", likes=8, sold=False, artist_id=1),
        Artwork(title="Mona Lisa", image="...", year=1503, price=100000, detail="...", likes=10, sold=False, artist_id=3),
        # Add more artworks...
    ]
    db.session.add_all(artworks)
    db.session.commit()

    # Create users
    users = [
        User(username='artlover1', password='password123', email='artlover1@example.com'),
        User(username='galleryfan', password='password456', email='galleryfan@example.com'),
        User(username='artcollector', password='password789', email='artcollector@example.com'),
    ]
    db.session.add_all(users)
    db.session.commit()

    # Create groups
    groups = [Group(name=f"group{i}") for i in range(1, 6)]
    db.session.add_all(groups)
    db.session.commit()

    # Associate users with groups
    users[0].groups.append(groups[0])
    users[1].groups.append(groups[1])
    db.session.commit()

    # Create posts
    posts = [
        Post(title="Post 1", content="Content for post 1", user=users[0]),
        # Add more posts...
    ]
    db.session.add_all(posts)
    db.session.commit()

    print("Database seeded successfully!")