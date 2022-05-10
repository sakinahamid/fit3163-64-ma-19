import React, { useState } from "react";
import axios from "axios";

import "./App.css";
import KnowledgeGraph from "./components/knowledge-graph/knowledge-graph.component";
import Popup from "./components/popup/Popup";

function App() {
  const [file, setFile] = useState();
  const [updated, setUpdated] = useState(false);

  function handleChange(event) {
    setFile(event.target.files[0]);
  }

  function handleSubmit(event) {
    event.preventDefault();
    const formData = new FormData();

    formData.append("file", file);

    axios
      .post("/api/upload", formData)
      .then((res) => {
        console.log(res);
        setUpdated(true);
      })
      .catch((err) => console.warn(err));
  }

  return (
    <>
      <h1>COVID-19 Knowledge Graph</h1>
      <form onSubmit={handleSubmit}>
        <p>Upload Article</p>
        <input type="file" onChange={handleChange}></input>
        <button type="submit">Submit</button>
      </form>
      <KnowledgeGraph updated={updated} />
    </>
  );
}

export default App;
