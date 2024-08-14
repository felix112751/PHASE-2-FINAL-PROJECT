import React from 'react'

function Contacts() {
  return (
    <div>
         <div className="container">
        <div className="row">
          <div className="col-md-4">
            <h5>Contact Us</h5>
            <p>Get in touch with us to learn more about our art gallery and upcoming exhibitions.</p>
          </div>
          <div className="col-md-4">
            <h5>Email</h5>
            <a href="mailto:info@artgallery.com">info@artgallery.com</a>
          </div>
          <div className="col-md-4">
            <h5>Social Media</h5>
            <ul className="social-links">
              <li>
                <a href="https://www.instagram.com/artgallery/" target="_blank" rel="noopener noreferrer">instragram
                  <i className="fab fa-instagram" aria-hidden="true"></i>
                </a>
              </li>
              <li>
                <a href="https://www.facebook.com/artgallery/" target="_blank" rel="noopener noreferrer">Facebook
                  <i className="fab fa-facebook-f" aria-hidden="true"></i>
                </a>
              </li>
              <li>
                <a href="https://twitter.com/artgallery" target="_blank" rel="noopener noreferrer">twitter
                  <i className="fab fa-twitter" aria-hidden="true"></i>
                </a>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  )
}

export default Contacts;






;