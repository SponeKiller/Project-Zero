
import React from "react";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";

import Homepage from "./features/homepage/index.js"
import Registration from "./features/registration/index.js"

function App() {
    return (
      <div className="App">
        <Router>
            <Routes>
                <Route path="/" element={<Homepage />} />
                <Route path="/register" element={<Registration />} />
            </Routes>
        </Router>
      </div>
    );
  }


  export default App;