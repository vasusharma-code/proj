import React from "react";

const MainContent = () => (
  <div className="flex-1 bg-white p-8 overflow-hidden">
    <div>
      <h2 className="text-3xl font-bold mb-4 text-gray-800">
        Welcome to the Main Content Area
      </h2>
      <p className="text-gray-600 leading-relaxed">
        Explore this section to learn more about our amazing features and services.
      </p>
      <button className="mt-6 bg-blue-600 text-white px-6 py-2 rounded shadow hover:bg-blue-700">
        Get Started
      </button>
    </div>
  </div>
);

export default MainContent;
