import React from 'react';
import { Link } from 'react-router-dom';

const Header: React.FC = () => {
  return (
    <header className="bg-white shadow-sm">
      <nav className="container mx-auto px-4 py-4">
        <div className="flex items-center justify-between">
          <Link to="/" className="text-2xl font-bold text-primary-600">
            E-Learning Platform
          </Link>
          
          <div className="flex items-center space-x-4">
            <Link to="/courses" className="text-gray-600 hover:text-primary-600">
              Courses
            </Link>
            <Link to="/login" className="btn btn-outline">
              Login
            </Link>
            <Link to="/signup" className="btn btn-primary">
              Sign Up
            </Link>
          </div>
        </div>
      </nav>
    </header>
  );
};

export default Header; 