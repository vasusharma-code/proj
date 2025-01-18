import React from "react";

const Navbar = () => (
  <nav className="bg-gradient-to-r from-blue-500 via-blue-600 to-blue-700 text-white fixed top-0 w-full z-50 shadow-lg">
    <div className="container mx-auto px-4 py-3 flex justify-between items-center">
      <h1 className="text-lg font-bold tracking-wide">Responsive Webpage</h1>
      <ul className="flex space-x-6">
        <li className="hover:underline cursor-pointer">Home</li>
        <li className="hover:underline cursor-pointer">About</li>
        <li className="hover:underline cursor-pointer">Contact</li>
      </ul>
    </div>
  </nav>
);

export default Navbar;
