// src/components/CategoryDropdown.js

import React from 'react';

const CategoryDropdown = ({ category }) => {
  return (
    <div className="category-dropdown card">
      <div className="card-body">
        <label htmlFor={`category-${category.id}`} className="form-label">{category.name}</label>
        <select id={`category-${category.id}`} className="form-select">
          <option value="example1">Example 1</option>
          <option value="example2">Example 2</option>
        </select>
      </div>
    </div>
  );
};

export default CategoryDropdown;
