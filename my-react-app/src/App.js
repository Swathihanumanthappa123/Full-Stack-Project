import './App.css';
import React, { useState, useEffect } from 'react';
import axios from 'axios';

const App = () => {
  const [authors, setAuthors] = useState([]);

  useEffect(() => {
    const fetchAuthors = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:8000/top-authors');
        setAuthors(response.data);
      } catch (error) {
        console.error('Error fetching authors:', error);
      }
    };

    fetchAuthors();
  }, []);

  return (
  <div>
      <div classname="navigation">
                      <nav>
                          <img src="/images/krikey-logo.jpg" className="logo"/>
                          <ul className="menu">
                              <li><a href="#">How to Animate<span class="dropdown-symbol">&#9662;</span></a></li>
                              <li><a href="#">Business<span class="dropdown-symbol">&#9662;</span></a></li>
                              <li><a href="#">Education<span class="dropdown-symbol">&#9662;</span></a></li>
                              <li><a href="#">Social Media<span class="dropdown-symbol">&#9662;</span></a></li>
                              <li><a href="#">Pricing</a></li>
                              <li><a href="#">About Us</a></li>
                          </ul>
                          <button type ="button">Get Started</button>
                      </nav>
      </div>
        <div className="container">
            <h1 className="heading">Top Authors</h1>
            <div className="author-list">
            {authors.map((author) => (
              <ul>
                <list key={author.author_name} className="author-card">
                    <img src="/images/placeholder.png" className="profile-img" />
                    <h3>{author.author_name}</h3>
                    <p>Total Revenue: ${author.total_revenue}</p>
                </list>
              </ul>
            ))}
            </div>
        </div>
  </div>
    );
  };

export default App;
