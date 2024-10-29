import React, { useState } from "react";
import "./AddArt.css";
import Navbar from "./Navbar";

function AddArt({ onAddArt }) {
  const [title, setTitle] = useState("");
  const [artistId, setArtistId] = useState(""); // Assuming you will use artist ID
  const [image, setImage] = useState("");
  const [year, setYear] = useState("");
  const [price, setPrice] = useState("");
  const [detail, setDetail] = useState("");

  const handleSubmit = (event) => {
    event.preventDefault();

    const newArt = {
      title,
      artist_id: artistId, // Use artist ID instead of name
      image,
      year,
      likes: 0,
      price,
      sold: false,
      detail,
    };

    fetch("http://127.0.0.1:5000/artworks", {
      // Ensure this is correct
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(newArt),
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error("Failed to create artwork");
        }
        return response.json();
      })
      .then((data) => {
        onAddArt(data);
        // Clear form fields
        setTitle("");
        setArtistId(""); // Reset artist ID as well
        setImage("");
        setYear("");
        setPrice("");
        setDetail("");
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  };

  return (
    <>
      <Navbar />
      <div className="mein">
        <form onSubmit={handleSubmit} className="add-art-container">
          <h2>Add New Art</h2>
          <label>
            Title:
            <input
              type="text"
              value={title}
              onChange={(e) => setTitle(e.target.value)}
              placeholder="Enter art title"
            />
          </label>
          <label>
            Artist ID: {/* Assuming artist ID input or selection */}
            <input
              type="text"
              value={artistId}
              onChange={(e) => setArtistId(e.target.value)}
              placeholder="Enter artist ID" // Use artist ID input
            />
          </label>
          <label>
            Image URL:
            <input
              type="text"
              value={image}
              onChange={(e) => setImage(e.target.value)}
              placeholder="Enter image URL"
            />
          </label>
          <label>
            Year:
            <input
              type="number"
              value={year}
              onChange={(e) => setYear(e.target.value)}
              placeholder="Enter year of creation"
            />
          </label>
          <label>
            Price:
            <input
              type="number"
              value={price}
              onChange={(e) => setPrice(e.target.value)}
              placeholder="Enter price"
            />
          </label>
          <label>
            Detail:
            <textarea
              value={detail}
              onChange={(e) => setDetail(e.target.value)}
              placeholder="Enter additional details"
            />
          </label>
          <button type="submit">Add Art</button>
        </form>
      </div>
    </>
  );
}

export default AddArt;
