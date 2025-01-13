import React, { useEffect } from "react";
import Navbar from "./components/Navbar";
import LeftMenu from "./components/LeftMenu";
import MainContent from "./components/MainContent";
import RightPanel from "./components/RightPanel";
import Footer from "./components/Footer";

const App = () => {
  // Page shrinking logic
  const shrinkPage = () => {
    const width = window.innerWidth;
    const body = document.body;

    if (width >= 992 && width <= 1600) {
      body.style.transform = "scale(0.9)";
      body.style.transformOrigin = "top center";
    } else if (width >= 700 && width < 767) {
      body.style.transform = "scale(0.8)";
      body.style.transformOrigin = "top center";
    } else if (width >= 600 && width < 700) {
      body.style.transform = "scale(0.75)";
      body.style.transformOrigin = "top center";
    } else if (width <= 600) {
      body.style.transform = "scale(0.5)";
      body.style.transformOrigin = "top center";
    } else {
      body.style.transform = "scale(1)";
      body.style.transformOrigin = "top center";
    }
  };

  useEffect(() => {
    window.addEventListener("resize", shrinkPage);
    shrinkPage(); // Initial call
    return () => window.removeEventListener("resize", shrinkPage);
  }, []);

  // Layout with all components
  return (
    <div className="flex flex-col min-h-screen">
      <Navbar />
      <div className="flex flex-1 mt-[64px]"> {/* Add margin to adjust for fixed navbar */}
        <LeftMenu />
        <MainContent />
        <RightPanel />
      </div>
      <Footer />
    </div>
  );
};

export default App;
