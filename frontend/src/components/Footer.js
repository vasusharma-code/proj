import React from "react";

const Footer = () => (
  <footer className="bg-blue-600 text-white text-center py-6 mt-auto shadow-inner">
    <p>&copy; 2025 Responsive Webpage. All rights reserved.</p>
    <p className="text-sm">
      Crafted with ❤️.
    </p>
    <div className="flex justify-center space-x-4 mt-3">
      <a href="#" className="hover:underline">Privacy Policy</a>
      <a href="#" className="hover:underline">Terms of Service</a>
    </div>
  </footer>
);

export default Footer;

