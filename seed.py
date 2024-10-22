from app import app, db
from models import User, Post, Group, Artwork, Artist, Cart

with app.app_context():
    db.drop_all()
    db.create_all()

    db.session.query(User).delete()
    db.session.query(Post).delete()
    db.session.query(Group).delete()
    db.session.query(Artwork).delete()
    db.session.query(Artist).delete()
    db.session.commit()

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

   artworks = [
    Artwork(title="Starry Night", image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQoiXokZHJc3iND6Uqax-iQ-nU6PmC5lRPqIw&s", year=1889, price=5000, detail="Starry Night is one of Vincent van Gogh's most iconic paintings, created in 1889. It depicts a swirling night sky over a tranquil village, with bold, expressive brushstrokes capturing the motion of the stars and the moon. This masterpiece is celebrated for its emotional intensity, innovative use of color, and dramatic brushwork.", likes=8, sold=False, artist_id=1),
    
    Artwork(title="Mona Lisa", image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ0s5B5TIgNtd8NBG31BBu2v1cCxIZi3AEE2g&s", year=1503, price=100000, detail="The Mona Lisa is a portrait painting by the Italian Renaissance artist Leonardo da Vinci, completed between 1503 and 1506. It is renowned for its sophisticated use of sfumato and the enigmatic expression of the woman in the portrait.", likes=10, sold=False, artist_id=2),
    
    Artwork(title="The Persistence", image="https://cdn.britannica.com/96/240496-138-66D89FAD/Salvador-Dali-Persistence-of-Memory.jpg?w=800&h=450&c=crop", year=1931, price=20000, detail="The painting presents a dream-like landscape where time appears to dissolve. Soft, melting clocks suggest the malleability and subjective nature of time.", likes=8, sold=False, artist_id=3),
    
    Artwork(title="The Scream", image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS1kStiFO1k0-RIzz6I4MAXcPt1C4sdYSvV7A&s", year=1893, price=60000, detail="The Scream by Edvard Munch is a renowned expressionist painting depicting a figure on a bridge against a turbulent sky, capturing intense emotion and anxiety.", likes=8, sold=False, artist_id=4),
    
    Artwork(title="Girl with a Pearl Earring", image="https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/1665_Girl_with_a_Pearl_Earring.jpg/800px-1665_Girl_with_a_Pearl_Earring.jpg", year=1665, price=80000, detail="This iconic painting features a young girl wearing an exotic turban and a large pearl earring, celebrated for its captivating gaze and masterful portrayal of light.", likes=9, sold=False, artist_id=5),
    
    Artwork(title="Guernica", image="https://upload.wikimedia.org/wikipedia/en/thumb/7/74/PicassoGuernica.jpg/400px-PicassoGuernica.jpg", year=1937, price=30000, detail="Guernica is a mural painting by Pablo Picasso that depicts the horrors of war, using a monochromatic palette to convey chaos and destruction.", likes=12, sold=False, artist_id=6),
    
    Artwork(title="The Night Watch", image="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/The_Night_Watch_-_HD.jpg/1200px-The_Night_Watch_-_HD.jpg", year=1642, price=20002, detail="The Night Watch captures a dynamic scene of a militia company, notable for its use of light and shadow to create a sense of movement.", likes=6, sold=False, artist_id=7),
    
    Artwork(title="The Birth of Venus", image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR9v3SJUhLh65lLuJo-3nsm4cPguDQb_4mGyg&s", year=1486, price=400000, detail="This painting depicts the mythological birth of Venus, celebrated for its graceful composition and Botticelli's mastery of line and detail.", likes=13, sold=False, artist_id=8),
    
    Artwork(title="American Gothic", image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRjVnMwqihzhYhxYeyEr6qvyGlD_mbAz3NK7Q&s", year=1930, price=34000, detail="American Gothic portrays a stern man and woman in front of a farmhouse, often interpreted as a commentary on rural American values.", likes=4, sold=False, artist_id=9),
    
    Artwork(title="The Kiss", image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS87titbSUj74DnfP14bZn4stGqggtO8C2vjw&s", year=1908, price=10000, detail="The Kiss is known for its use of gold leaf and intricate patterns, symbolizing the sensuality of the romantic bond it portrays.", likes=13, sold=False, artist_id=10),
]

    db.session.add_all(artworks)
    db.session.commit()

    users = [
        User(username='artlover1', password='password123', email='artlover1@example.com'),
        User(username='galleryfan', password='password456', email='galleryfan@example.com'),
        User(username='artcollector', password='password789', email='artcollector@example.com'),
    ]
    db.session.add_all(users)
    db.session.commit()

    groups = [Group(name=f"group{i}") for i in range(1, 6)]
    db.session.add_all(groups)
    db.session.commit()

    users[0].groups.append(groups[0])
    users[1].groups.append(groups[1])
    db.session.commit()

    posts = [
        Post(title="Post 1", content="Content for post 1", user=users[0]),
    ]
    db.session.add_all(posts)
    db.session.commit()

    print("Database seeded successfully!")