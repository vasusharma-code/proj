import React, { useState } from "react";

const LeftMenu = () => {
  const [collapsed, setCollapsed] = useState(false);

  return (
    <div
      className={`bg-gray-100 p-4 border-r shadow-lg ${
        collapsed ? "w-16" : "w-64"
      } transition-all duration-500`}
    >
      <button
        className="bg-blue-600 text-white px-4 py-2 rounded-full mb-4 transition-transform transform hover:scale-105"
        onClick={() => setCollapsed(!collapsed)}
      >
        {collapsed ? ">" : "<"}
      </button>
      <ul className={`space-y-4 ${collapsed && "hidden"}`}>
        <li className="p-3 bg-gray-200 rounded-lg shadow hover:bg-blue-100 cursor-pointer">
          Dashboard
        </li>
        <li className="p-3 bg-gray-200 rounded-lg shadow hover:bg-blue-100 cursor-pointer">
          Settings
        </li>
        <li className="p-3 bg-gray-200 rounded-lg shadow hover:bg-blue-100 cursor-pointer">
          Profile
        </li>
      </ul>
    </div>
  );
};

export default LeftMenu;
