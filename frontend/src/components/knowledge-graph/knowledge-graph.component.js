import React, { useState, useEffect } from "react";
import { ForceGraph2D } from "react-force-graph";

import data_2 from "../../data_2.json";
import UpdateGraph from "./update-graph.component";
import Popup from "../popup/Popup";

function KnowledgeGraph() {
  const [json, setJson] = useState();
  const [btnPopup, setBtnPopup] = useState(false);
  const [node, setNode] = useState({});
  const [articles, setArticles] = useState([]);

  const mapArray = articles.map((article) => {
    return <li>{article}</li>;
  });

  useEffect(() => {
    fetch("/data").then((res) => {
      res.json().then((d) => {
        setJson(d);
      });
    });
  }, []);

  const onUpdate = () => {
    setJson(({ nodes, links }) => {
      console.log(data_2.nodes);
      return {
        nodes: nodes.concat(data_2.nodes),
        links: links.concat(data_2.links),
      };
    });
    console.log(json);
  };

  const onClick = (node) => {
    setNode(node);
    setArticles(node.articles);
    setBtnPopup(true);
  };

  return (
    <>
      <div className="upload-container">
        <UpdateGraph onUpdate={onUpdate} />
      </div>

      <ForceGraph2D
        graphData={json}
        nodeAutoColorBy={"group"}
        linkLabel={"label"}
        linkDirectionalArrowLength={4}
        linkDirectionalArrowRelPos={1}
        linkDirectionalParticleSpeed={0.005}
        linkDirectionalParticleWidth={1.5}
        linkDirectionalParticles={3}
        onNodeClick={(node) => {
          onClick(node);
        }}
      />
      <Popup trigger={btnPopup} setTrigger={setBtnPopup}>
        <h3>{node.name}</h3>
        <br />
        <ul>{mapArray}</ul>
      </Popup>
    </>
  );
}

export default KnowledgeGraph;
