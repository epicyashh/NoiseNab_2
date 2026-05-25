import React from "react";
import { BrowserRouter as Router, Routes, Route, Navigate } from "react-router-dom";
import NoiseDataEntry from "./NoiseDataEntry";
import NoiseMap from "./NoiseMap";
import Landing from "./Landing";
import "./App.css";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Landing />} />
        <Route path="/enter-noise-data" element={<NoiseDataEntry />} />
        <Route path="/noise-map" element={<NoiseMap />} />
        <Route
          path="/hotspot-map"
          element={
            <div style={{ width: "100vw", height: "100vh" }}>
              <iframe
                src="/map.html"
                style={{ width: "100%", height: "100%", border: "none" }}
                title="Hotspot Map"
              />
            </div>
          }
        />
        <Route path="*" element={<Navigate to="/" replace />} />
      </Routes>
    </Router>
  );
}

export default App;
