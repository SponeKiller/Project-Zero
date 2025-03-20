import React from "react";
import "./Homepage.css";
import Navbar from "../../components/ui/js/Navbar.js";
import Footer from "../../components/ui/js/Footer.js";

const Homepage = () => {
  return (

      <div className="homepage">
        <Navbar />
        <header className="hero-section">
          <h1>Welcome to Project Zero</h1>
          <p>Your journey to innovation starts here.</p>
          <a href="#features" className="cta-button">Learn More</a>
        </header>
        
        <section id="features" className="features">
          <h2>Features</h2>
          <div className="feature-list">
            <div className="feature-item">
              <h3>Feature 1</h3>
              <p>Detail about this amazing feature.</p>
            </div>
            <div className="feature-item">
              <h3>Feature 2</h3>
              <p>Detail about another incredible feature.</p>
            </div>
            <div className="feature-item">
              <h3>Feature 3</h3>
              <p>Why you will love this feature.</p>
            </div>
          </div>
        </section>
        
        <section id="about" className="about">
          <h2>About Project Zero</h2>
          <p>
            Project Zero is an innovative platform designed to simplify your life. 
            From powerful tools to seamless integration, we’ve got everything covered.
          </p>
        </section>
        <Footer />
      </div>
      
  );
};

export default Homepage;
