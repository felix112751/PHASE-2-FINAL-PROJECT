import React from "react";
import { useParams } from "react-router-dom";

function ArtDetail({ artworks, onLike, onAddToCart }) {
  const { id } = useParams();
  const art = artworks.find((art) => art.id === id); 

  if (!art) {
    return <p>Art not found!</p>;
  }

  const handleLike = () => {
    onLike(art.id);
  };

  const handleAddToCart = () => {
    onAddToCart(art.id);
  };

  return (
    <div>
      <h2>{art.title}</h2>
      <img src={art.image} alt={art.title} />
      <p>Artist: {art.artist}</p>
      <p>Year: {art.year}</p>
      <p>Price: ${art.price}</p>
      <p>Details: {art.detail}</p>
      <p>Likes: {art.likes}</p>
      <button onClick={handleLike}>Like</button>
      <button onClick={handleAddToCart} disabled={art.sold}>
        {art.sold ? "Sold Out" : "Add to Cart"}
      </button>
    </div>
  );
}

export default ArtDetail;