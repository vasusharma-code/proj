import React, { useEffect } from "react";
import Navbar from "./components/Navbar";
import LeftMenu from "./components/LeftMenu";
import MainContent from "./components/MainContent";
import RightPanel from "./components/RightPanel";
import Footer from "./components/Footer";

const App = () => {
  const shrinkPage = () => {
    const width = window.innerWidth;
    const body = document.body;

    if (width < 992) {
      const scale = Math.max(width / 1200, 0.5);
      body.style.transform = `scale(${scale})`;
      body.style.transformOrigin = "top center";
    } else {
      body.style.transform = "scale(1)";
      body.style.transformOrigin = "top center";
    }
  };

  useEffect(() => {
    window.addEventListener("resize", shrinkPage);
    shrinkPage();
    return () => window.removeEventListener("resize", shrinkPage);
  }, []);

  return (
    <div className="flex flex-col min-h-screen">
      <Navbar />
      <div className="flex flex-1 mt-[64px]">
        <LeftMenu />
        <MainContent />
        <RightPanel />
      </div>
      <Footer />
    </div>
  );
};

export default App;
