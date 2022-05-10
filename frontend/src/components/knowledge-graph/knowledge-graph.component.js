import React, { useState, useEffect } from "react";
import { ForceGraph2D } from "react-force-graph";

import data_2 from "../../data_2.json";
import UpdateGraph from "./update-graph.component";
import Popup from "../popup/Popup";

function KnowledgeGraph(props) {
  const [json, setJson] = useState();
  const [btnPopup, setBtnPopup] = useState(false);
  const [node, setNode] = useState({});
  const [articles, setArticles] = useState([]);
  const [jsonUpdate, setJsonUpdate] = useState();

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

  useEffect(() => {
    fetch("/update").then((res) => {
      res.json().then((d) => {
        setJsonUpdate(d);
      });
      if (jsonUpdate) {
        onUpdate();
      }
    });
  }, [props.updated]);

  const onUpdate = () => {
    setJson(({ nodes, links }) => {
      return {
        nodes: nodes.concat(jsonUpdate.nodes),
        links: links.concat(jsonUpdate.links),
      };
    });
  };

  const onClick = (node) => {
    setNode(node);
    if (node.articles) {
      setArticles(node.articles);
      console.log(props.updated);
    } else {
      setArticles([]);
    }

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
        d3Force={"link"}
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
