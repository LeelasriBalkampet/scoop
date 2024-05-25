// src/components/Home.js

import React, { useEffect, useState } from 'react';
import CategoryDropdown from './CategoryDropdown';
import './home.css'; // Import the custom CSS

const Home = () => {
  const [categories, setCategories] = useState([]);

  useEffect(() => {
    fetch('http://localhost:8000/api/categories/')
      .then(response => response.json())
      .then(data => setCategories(data))
      .catch(error => console.error('Error fetching categories:', error));
  }, []);

  return (
    <div className="container my-5">
      <header className="text-center mb-4">
        <h1>Welcome to Local News Platform</h1>
        <p className="lead">Your source for community news, events, and updates.</p>
      </header>
      <nav className="text-center mb-4">
        <ul className="nav justify-content-center">
          <li className="nav-item">
            <a className="nav-link" href="#recent-articles">Recent Articles</a>
          </li>
          <li className="nav-item">
            <a className="nav-link" href="#upcoming-events">Upcoming Events</a>
          </li>
          <li className="nav-item">
            <a className="nav-link" href="#popular-categories">Popular Categories</a>
          </li>
        </ul>
      </nav>
      <main>
        <section id="recent-articles" className="mb-5">
          <h2 className="text-center mb-3">Recent Articles</h2>
          {<text></text>}
        </section>
        <section id="upcoming-events" className="mb-5">
          <h2 className="text-center mb-3">Upcoming Events</h2>
          {/* Add event components here */}
        </section>
        <section id="popular-categories">
          <h2 className="text-center mb-3">Popular Categories</h2>
          <div className="row">
            {categories.map(category => (
              <div key={category.id} className="col-md-4 mb-3">
                <CategoryDropdown category={category} />
              </div>
            ))}
          </div>
        </section>
      </main>
      <footer className="text-center mt-5">
        <p>&copy; 2024 Local News Platform. All rights reserved.</p>
      </footer>
    </div>
  );
};

export default Home;

