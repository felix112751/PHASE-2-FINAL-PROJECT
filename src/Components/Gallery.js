import React from "react";
import { Link } from "react-router-dom";

function Gallery({ artworks }) {
  return (
    <div>
      <h2>Gallery</h2>
      <div className="art-list">
        {artworks.map((art) => (
          <div key={art.id} className="art-card">
            <h3>{art.title}</h3>
            <img src={art.image} alt={art.title} />
            <p>Price: ${art.price}</p>
            <p>Likes: {art.likes}</p>
            <p>{art.sold ? "Sold Out" : "Available"}</p>
            <Link to={`/art/${art.id}`}>View Details</Link>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Gallery;
