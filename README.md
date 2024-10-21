![GitHub contributors](https://img.shields.io/github/contributors-anon/felix112751/PHASE-2-FINAL-PROJECT?style=for-the-badge&logoColor=green&logoSize=60px&labelColor=blue&color=green-blue)
![GitHub forks](https://img.shields.io/github/forks/felix112751/PHASE-2-FINAL-PROJECT?style=for-the-badge&labelColor=blue&color=yellow)


# PHASE 4 PROJECT

## VIRTUAL ART PROJECT

## *Overview*

Virtual Art Project is an e-commerce platform that has been built using React. The platform allows users to browse, like and purchase artworks, the platform also adds artworks for sellers who want to sell their art and it also provides a basic shopping cart functionality. 

The platform enables users to add their artwork for sale and offers a shopping cart feature to manage potential purchases.

This project has been developed using a combination of React for the frontend and Flask with SQLAlchemy for the backend.

THe backend manages user data, artwork information and shopping cart functionality and the frontend provides an interactive user experience

## *Features*

- Browse artworks in the gallery.
- View details of individual artworks.
- Add artworks to shopping cart.
- Remove artworks from the shopping cart.
- Like artworks to show appreciation.
- Lets the users add their artwork.

## *Project Details*

- Built using React and React outer for client-side routing.
- Uses backend API to manage artwork data.

- The following languages were used:

[![React](https://img.shields.io/badge/React-JS-navy?style=for-the-badge&labelColor=black&logo=react&logoColor=blue)](https://reactjs.org/)

[![JavaScript](https://img.shields.io/badge/JavaScript-JS-gold?style=for-the-badge&labelColor=black&logo=javascript)](https://www.javascript.com/)

[![Python](https://img.shields.io/badge/Python-3-blue?style=for-the-badge&labelColor=gold&logo=python)](https://www.python.org/)

[![Flask](https://img.shields.io/badge/Flask-Framework-red?style=for-the-badge&labelColor=blue&logo=flask)](https://flask.palletsprojects.com/)

[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-red?style=for-the-badge&labelColor=grey&logo=sqlalchemy)](https://www.sqlalchemy.org/)

## *Components*

1. `Navbar`: A navigation bar component that provides links to different routes.
2. `Home`: A home page component that displays the landing page which includes a welcome message.
3. `Gallery`: A gallery component that displays a list of artworks.
4. `AddArt`: A component that allows users to add new artworks.
5. `ArtDetails`: A component that displays the details of an individual artwork.
5. `Cart`: A shopping cart component that displays the artworks added by the user.

## Frontend API Requests
- `Fetch Artworks`: Retrieves the list of artworks (*GET /artworks*).
- `Submit Arwork`: Adds a new artwork to the system (*POST /artworks.*).
- `Fetch Cart`: Retrieves the user's shopping cart (*GET/users/:user_id/cart*).
- `Add To Cart`: Adds an artwork to the user's shopping cart (*POST /users/:user_id/cart*).
## Installation

To run the frontend:

1. #### Clone the repository:

```bash
git clone
cd PHASE-2-FINAL-PROJECT
```

2. #### Set up JSON Server:

Ensure you have JSON server installed. If not, install it using npm:

```bash
npm install -g json-server
```

3. #### Create db.json file:

A db.json file was provided containing the 10 objects containing the title, artist name, image, year, likes, price of artwork, artworks sold and details of each artwork. Here is an example:

```bash
    {
      "id": "1",
      "title": "Starry Night",
      "artist": "Vincent van Gogh",
      "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQoiXokZHJc3iND6Uqax-iQ-nU6PmC5lRPqIw&s",
      "year": 1889,
      "likes": 8,
      "price": 5000,
      "sold": false,
      "detail": " Starry Night is one of Vincent van Gogh's most iconic paintings, created in 1889. It depicts a swirling night sky over a tranquil village, with bold, expressive brushstrokes capturing the motion of the stars and the moon. The scene is framed by a dark cypress tree in the foreground, contrasting against the vibrant, star-filled sky. This masterpiece is celebrated for its emotional intensity, innovative use of color, and dramatic brushwork, reflecting van Gogh's turbulent state of mind and his fascination with the cosmos."
    },
    {
      "id": "2",
      "title": "Mona Lisa",
      "artist": "Leonardo da Vinci",
      "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ0s5B5TIgNtd8NBG31BBu2v1cCxIZi3AEE2g&s",
      "year": 1503,
      "likes": 10,
      "price": 100000,
      "sold": false,
      "detail": "The Mona Lisa is a portrait painting by the Italian Renaissance artist Leonardo da Vinci, completed between 1503 and 1506. The artwork depicts a woman with an enigmatic expression, famously known for her subtle smile. It is renowned for its sophisticated use of sfumato—a technique that creates a soft, gradual transition between colors and tones. The painting is housed in the Louvre Museum in Paris and is considered one of the most iconic and celebrated artworks in the world. The identity of the woman in the portrait, often believed to be Lisa Gherardini, remains a topic of debate and intrigue."
    }
```
#### 4. Run the JSON server:
Start the server by running the following command in the project directory:

```bash
json-server --watch db.json

```

## Backend Details
The backend is built using **Flask** with **SQLAlchemy** for database management. It handles user data, artwork details and shopping cart functionality

### Backend Models
1. **Artist**
- Stores information about the artist.
- Attributes: id, name, bio, image
2. **Artwork**
- Stores information about the artwork such as the title, image, year, price and likes.
- Attributes: id, title, artist, image, year, likes, price
3. **Cart**
- Stores information about the user's shopping cart.
- Attributes: id, user_id, artworks, total_price
4. **User**
- Stores information about the user such as username, password and email.
- Attributes: id, username, password, email
### Backend API Endpoints
- **Artists**:
  - `GET /artists`: Retrieve a list of all artists.
  - `POST /artists`: Create a new artist.

- **Artworks**:
  - `GET /artworks`: Retrieve a list of all artworks.
  - `POST /artworks`: Create a new artwork.
  - `GET /artworks/:id`: Retrieve details of a specific artwork.
  - `DELETE /artworks/:id`: Delete a specific artwork.

- **Carts**:
  - `GET /users/:user_id/cart`: Retrieve the user's shopping cart.
  - `POST /users/:user_id/cart`: Add artwork(s) to the user's shopping cart.
  - `DELETE /users/:user_id/cart`: Remove artwork(s) from the user's shopping cart.

- **Users**:
  - `GET /users`: Retrieve a list of all users.
  - `POST /users`: Create a new user.

### Backend Installation
To run this project this locally:

1. Clone the repository:
```bash
git clone https://github.com/felix112751/art-gallery.git
cd art-gallery
```
2. Install dependencies
```bash
pip install -r requirements.txt
```
3. Create a virtual environment:
```bash
python -m venv venv
```
4. Activate the virtual environment:
```bash
source venv/bin/activate
```
5. Set up the database:
```bash
flask db init
flask db migrate
flask db upgrade
```
6. Run the server:
```bash
flask run
```

## Contributors ✨

Thanks to these wonderful people for their contributions:

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/felix112751">
        <img src="https://avatars.githubusercontent.com/u/172261865?v=4" width="100px;" alt="Felix Goyeh"/><br />
        <sub><b>Felix Goyeh</b></sub>
      </a><br />
      <a href="#" title="Code">💻</a>
    </td>
    <td align="center">
      <a href="https://github.com/Yussuf-ibra">
        <img src="https://avatars.githubusercontent.com/u/172136288?v=4" width="100px;" alt="Yussuf Ibrahim"/><br />
        <sub><b>Yussuf Ibrahim</b></sub>
      </a><br />
      <a href="#" title="Documentation">📖</a>
    </td>
    <td align="center">
      <a href="https://github.com/Mars254">
        <img src="https://avatars.githubusercontent.com/u/174427461?v=4" width="100px;" alt="Mark Kamau"/><br />
        <sub><b>Mark Kamau</b></sub>
      </a><br />
      <a href="#" title="Code">💻</a>
    </td>
    <td align="center">
      <a href="https://github.com/mburufiona">
        <img src="https://avatars.githubusercontent.com/u/172260583?s=400&u=7c8ebfe708a5be75eb9e479e0119b19a53ffb757&v=4" width="100px;" alt="Fiona Mburu"/><br />
        <sub><b>Fiona Mburu</b></sub>
      </a><br />
      <a href="#" title="Testing">⚠️</a>
    </td>
    <td align="center">
      <a href="https://github.com/maajidmuhammad/python-p4-chatterbox-lab">
        <img src="https://avatars.githubusercontent.com/u/162092453?v=4" width="100px;" alt="Maajid Muhammad"/><br />
        <sub><b>Maajid Muhammad</b></sub>
      </a><br />
      <a href="#" title="Code">💻</a>
    </td>
  </tr>
</table>



This project is open-source and available under the MIT License.

### Deployed Link.