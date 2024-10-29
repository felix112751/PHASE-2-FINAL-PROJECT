import React, { useState, useEffect } from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
// import Navbar from "./Components/Navbar";
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
    fetch("https://phase-2-final-project-1.onrender.com/artworks", {
      method: "GET",
      headers: { "Content-Type": "application/json" },
    })
      .then((response) => response.json())
      .then((data) => setArtworks(data))
      .catch((error) => console.error("Error fetching artworks:", error));
      
    }, []);

  const addArt = (newArt) => {
    setArtworks([...artworks, newArt]);
    
  };

  const likeArt = (id) => {
    const updatedArtworks = artworks.map((art) =>
      art.id === id ? { ...art, likes: art.likes + 1 } : art
    );
    setArtworks(updatedArtworks);

    fetch(`https://phase-2-final-project-1.onrender.com/artworks/${id}`, {
      method: "PATCH",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        likes: updatedArtworks.find((art) => art.id === id).likes,
      }),
    }).catch((error) => console.error("Error updating likes:", error));
  };

  const addToCart = (id) => {
    const art = artworks.find((art) => art.id === id);
    if (art && !art.sold) {
      setCart([...cart, art]);
      setArtworks(
        artworks.map((a) => (a.id === id ? { ...a, sold: true } : a))
      );

      fetch(`https://phase-2-final-project-1.onrender.com/artworks/${id}`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ sold: true }),
      }).catch((error) => console.error("Error updating sold status:", error));
    }
  };

  const removeFromCart = (id) => {
    setCart(cart.filter((item) => item.id !== id));
    setArtworks(artworks.map((a) => (a.id === id ? { ...a, sold: false } : a)));

    fetch(`https://phase-2-final-project-1.onrender.com/artworks/${id}`, {
      method: "PATCH",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ sold: false }),
    }).catch((error) => console.error("Error updating sold status:", error));
  };

  return (
    <Router>
      {/* Uncomment if Navbar component is available */}
      {/* <Navbar /> */}
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
