import React from "react";
import { Link } from "react-router-dom";
import "./Gallery.css"; // Import the CSS file
import Navbar from "./Navbar";


function Gallery({ artworks }) {
  return (
    <div className="odin">

<Navbar /> 
    <div className="gallery-container">
      <h2>Gallery</h2>
      <div className="art-list">
        {artworks.map((art) => (
          <div key={art.id} className="art-card">
            <h3>{art.title}</h3>
            <img src={art.image} alt={art.title} />
            <p>Price: ${art.price}</p>
            <p>Likes: {art.likes}</p>
            <p className={art.sold ? "sold-out" : "available"}>
              {art.sold ? "Sold Out" : "Available"}
            </p>
            <Link to={`/art/${art.id}`} className="button">View Details</Link>
          </div>
        ))}
      </div>
    </div>

    </div>
  );
}

export default Gallery;
