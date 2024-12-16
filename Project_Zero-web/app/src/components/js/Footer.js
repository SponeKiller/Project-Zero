import React from "react";
import "../css/Footer.css";

const Footer = () => {
  return (
    <footer className="footer">
      <p>© {new Date().getFullYear()} Project-Zero, inc. All Rights Reserved.</p>
      <ul className="footer-links">
        <li><a href="#privacy">Privacy Policy</a></li>
        <li><a href="#terms">Terms of Service</a></li>
        <li><a href="#contact">Contact Us</a></li>
      </ul>
    </footer>
  );
};

export default Footer;
