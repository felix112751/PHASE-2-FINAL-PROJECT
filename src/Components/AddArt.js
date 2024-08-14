import React, { useState } from "react";

function AddArt({ onAddArt }) {
  const [title, setTitle] = useState("");
  const [artist, setArtist] = useState("");
  const [image, setImage] = useState("");
  const [year, setYear] = useState("");
  const [price, setPrice] = useState("");
  const [detail, setDetail] = useState("");

  const handleSubmit = (event) => {
    event.preventDefault();

    const newArt = {
      title,
      artist,
      image,
      year,
      likes: 0,
      price,
      sold: false,
      detail,
    };

    fetch("https://artt-backend.vercel.app/artworks", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(newArt),
    })
      .then((response) => response.json())
      .then((data) => {
        onAddArt(data);
        setTitle("");
        setArtist("");
        setImage("");
        setYear("");
        setPrice("");
        setDetail("");
      });
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Add New Art</h2>
      <label>
        Title:
        <input
          type="text"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
        />
      </label>
      <label>
        Artist:
        <input
          type="text"
          value={artist}
          onChange={(e) => setArtist(e.target.value)}
        />
      </label>
      <label>
        Image URL:
        <input
          type="text"
          value={image}
          onChange={(e) => setImage(e.target.value)}
        />
      </label>
      <label>
        Year:
        <input
          type="number"
          value={year}
          onChange={(e) => setYear(e.target.value)}
        />
      </label>
      <label>
        Price:
        <input
          type="number"
          value={price}
          onChange={(e) => setPrice(e.target.value)}
        />
      </label>
      <label>
        Detail:
        <textarea value={detail} onChange={(e) => setDetail(e.target.value)} />
      </label>
      <button type="submit">Add Art</button>
    </form>
  );
}

export default AddArt;
