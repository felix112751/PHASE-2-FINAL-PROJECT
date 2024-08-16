import React, { useState, useEffect } from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Navbar from "./Components/Navbar";
import Home from "./Components/Home";
import Gallery from "./Components/Gallery";
import AddArt from "./Components/AddArt";
import Cart from "./Components/Cart";
import ArtDetails from "./Components/ArtDetails";
import Contacts from "./Components/Contacts";

function App() {
  const [artworks, setArtworks] = useState([]);
  const [cart, setCart] = useState([]);

  useEffect(() => {
    fetch("https://artt-backend.vercel.app/artworks")
      .then((response) => response.json())
      .then((data) => setArtworks(data));
  }, []);

  const addArt = (newArt) => {
    setArtworks([...artworks, newArt]);
  };

  const likeArt = (id) => {
    const updatedArtworks = artworks.map((art) =>
      art.id === id ? { ...art, likes: art.likes + 1 } : art
    );
    setArtworks(updatedArtworks);
    fetch(`https://artt-backend.vercel.app/artworks/${id}`, {
      method: "PATCH",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        likes: updatedArtworks.find((art) => art.id === id).likes,
      }),
    });
  };

  const addToCart = (id) => {
    const art = artworks.find((art) => art.id === id);
    if (art && !art.sold) {
      setCart([...cart, art]);
      setArtworks(
        artworks.map((a) => (a.id === id ? { ...a, sold: true } : a))
      );
      fetch(`https://artt-backend.vercel.app/artworks/${id}`, {
        method: "PATCH",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ sold: true }),
      });
    }
  };

  const removeFromCart = (id) => {
    setCart(cart.filter((item) => item.id !== id));
    setArtworks(artworks.map((a) => (a.id === id ? { ...a, sold: false } : a)));
    fetch(`https://artt-backend.vercel.app/artworks/${id}`, {
      method: "PATCH",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ sold: false }),
    });
  };

  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/gallery" element={<Gallery artworks={artworks} />} />
        <Route path="/add" element={<AddArt onAddArt={addArt} />} />
        <Route path="/contacts" element={<Contacts />} />
        <Route
          path="/cart"
          element={<Cart cartItems={cart} onRemoveFromCart={removeFromCart} />}
        />
        <Route
          path="/art/:id"
          element={
            <ArtDetails
              artworks={artworks}
              onLike={likeArt}
              onAddToCart={addToCart}
            />
          }
        />
      </Routes>
    </Router>
  );
}

export default App;
