import React from "react";

const RightPanel = () => (
  <div className="bg-gray-50 w-64 p-6 border-l shadow-lg">
    <h2 className="text-xl font-semibold mb-4 text-blue-700">
      Useful Information
    </h2>
    <p className="text-gray-500 leading-relaxed">
      Widgets, updates, and quick links can be placed here for easy access.
    </p>
    <div className="mt-6">
      <button className="bg-blue-600 text-white px-6 py-2 rounded shadow hover:bg-blue-700">
        Learn More
      </button>
    </div>
  </div>
);

export default RightPanel;
