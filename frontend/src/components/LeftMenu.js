import React, { useState } from "react";

const LeftMenu = () => {
  const [collapsed, setCollapsed] = useState(false);

  return (
    <div
      className={`bg-gray-100 p-4 border-r ${
        collapsed ? "w-16" : "w-64"
      } transition-all duration-300`}
    >
      <button
        className="bg-blue-600 text-white px-4 py-2 rounded mb-4"
        onClick={() => setCollapsed(!collapsed)}
      >
        {collapsed ? ">" : "<"}
      </button>
      {!collapsed && (
        <ul className="space-y-2">
          <li className="p-2 hover:bg-blue-100 rounded">Menu Item 1</li>
          <li className="p-2 hover:bg-blue-100 rounded">Menu Item 2</li>
          <li className="p-2 hover:bg-blue-100 rounded">Menu Item 3</li>
        </ul>
      )}
    </div>
  );
};

export default LeftMenu;
