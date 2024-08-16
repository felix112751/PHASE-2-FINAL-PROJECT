import React from "react";
import { Link } from "react-router-dom";
import "./Cart.css"; // Import the CSS file
import Navbar from "./Navbar";

function Cart({ cartItems, onRemoveFromCart }) {
  return (
<>
      <Navbar />
      <div className="cart-container">
            <h2 className="btn-shine">Shopping Cart</h2>
            {cartItems.length === 0 ? (
              <p>Your cart is empty.</p>
            ) : (
              <ul className="cart-list">
                {cartItems.map((item) => (
                  <li key={item.id}>
                    <img
                      src={item.image}
                      alt={item.title}
                      style={{ width: "100px", height: "100px" }}
                    />
                    <h3>{item.title}</h3>
                    <p>Price: ${item.price}</p>
                    <p>Likes: {item.likes}</p>
                    <button onClick={() => onRemoveFromCart(item.id)}>
                      Remove from Cart
                    </button>
                  </li>
                ))}
              </ul>
            )}
            <Link to="/">Back to Home</Link>
          </div>
</>
  );
}

export default Cart;
