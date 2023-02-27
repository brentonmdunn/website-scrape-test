import React from "react";
import logo from "./logo.svg";
import "./App.css";
import { Home } from "./components/Home";
import { CSV } from "./components/CSV";

function App() {
  return (
    <div>
      <Home />
      <CSV />
    </div>
  );
}

export default App;
