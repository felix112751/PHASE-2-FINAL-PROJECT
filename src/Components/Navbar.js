import React from "react";
import { Link } from "react-router-dom";
import "./Navbar.css"; 

function Navbar() {
  return (
   <div className="odin">
       <nav className="navbar">
      <div className="navbar-logo">
        <h2 className="bts-shine">Art Gallery</h2>
      </div>
      <ul className="navbar-links">
        <li><Link to="/">Home</Link></li>
        <hr/>
        <li><Link to="/gallery">Gallery</Link></li>
        <hr/>
        <li><Link to="/add">Add Art</Link></li>
        <hr/>
        <li><Link to="/art/1">ArtDetails</Link></li>
        <hr/>
        <li><Link to="/cart">Cart</Link></li>
      </ul>
    </nav>
    </div>
  );
}

export default Navbar;
