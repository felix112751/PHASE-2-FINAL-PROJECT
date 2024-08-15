# PHASE 2 PROJECT

## VIRTUAL ART PROJECT

## *Overview*

Virtual Art Project is an e-commerce platform that has been built using React. The platform allows users to browse, like and purchase artworks, the platform also adds artworks for sellers who want to sell their art and it also provides a basic shopping cart functionality. 

## *Functionality*

- Browse artworks in the gallery.
- View details of individual artworks.
- Add artworks to shopping cart.
- Remove artworks from the shopping cart.
- Like artworks to show appreciation.
- Lets the users add their artwork.

## *Project Details*

- Built using React and React outer for client-side routing.
- Uses backend API to manage artwork data.

## *Components*

1. `Navbar`: A navigation bar component that provides links to different routes.
2. `Home`: A home page component that displays the landing page which includes a welcome message.
3. `Gallery`: A gallery component that displays a list of artworks.
4. `AddArt`: A component that allows users to add new artworks.
5. `ArtDetails`: A component that displays the details of an individual artwork.
5. `Cart`: A shopping cart component that displays the artworks added by the user.

## *API Endpoints*

- `GET `: Retrieves a list of artworks from the backend API
- `POST `: Creates a new artwork in the backend API
- `PATCH `: Updates an existing artwork in the backend API

## Installation

To run this project locally, follow these steps:

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
### Contributors
This application was a group project that was created by 4 contributors:

- [Felix_Goyeh](https://github.com/felix112751)
- [Yussuf_Ibrahim](https://github.com/Yussuf-ibra)
- [Mark_Kamau](https://github.com/Mars254)
- [Fiona_Mburu](https://github.com/mburufiona)

This project is open-source and available under the MIT License.

### Deployed Link.