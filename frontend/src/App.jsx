import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import LandingPage from "./pages/LandingPage";
import ClaimsPage from "./pages/ClaimsPage";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<LandingPage />} />
        <Route path="/claims" element={<ClaimsPage />} />
      </Routes>
    </Router>
  );
}

export default App;
