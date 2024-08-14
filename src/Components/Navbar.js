import React from "react";
import { link } from "react-router-dom";

function Navbar() {
  return (
    <nav>
      <Link to="/">Home</Link>
      <Link to="/gallery">Gallery</Link>
      <Link to="/add">Add Art</Link>
      <Link to="/cart">Cart</Link>
    </nav>
  );
}

export default Navbar;
