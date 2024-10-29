import React from "react";
import { useParams } from "react-router-dom";
import styles from "./ArtDetail.module.css";
import Navbar from "./Navbar";

function ArtDetail({ artworks, onLike, onAddToCart }) {
  const { id } = useParams();
  const art = artworks.find((art) => art.id === parseInt(id));

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
    <>
      <Navbar />
      <div className={styles.artDetailContainer}>
        <h2 className={styles.artTitle}>{art.title}</h2>
        <img src={art.image} alt={art.title} className={styles.artImage} />
        <div className={styles.artContent}>
          {/* Check if artist exists before accessing its properties */}
          <p className={styles.artInfo}>
            Artist: {art.artist ? art.artist.name : "Unknown"}
          </p>
          <p className={styles.artInfo}>Year: {art.year}</p>
          <p className={styles.artPrice}>Price: ${art.price}</p>
          <p className={styles.artDetails}>Details: {art.detail}</p>
          <p className={styles.artLikes}>
            <i className="fa-solid fa-heart fa-fade"></i>: {art.likes}
          </p>
          <button
            className={`${styles.button} ${styles.likeButton}`}
            onClick={handleLike}
          >
            Like
          </button>
          <button
            className={`${styles.button} ${styles.addToCartButton}`}
            onClick={handleAddToCart}
            disabled={art.sold}
          >
            {art.sold ? "Sold Out" : "Add to Cart"}
          </button>
        </div>
      </div>
    </>
  );
}

export default ArtDetail;
