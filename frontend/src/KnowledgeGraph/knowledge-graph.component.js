import React, { useState, useEffect } from "react";
import { ForceGraph2D } from "react-force-graph";

import data from "../data.json";
import data_2 from "../data_2.json";
import UpdateGraph from "./update-graph.component";

function KnowledgeGraph() {
  const [test, setTest] = useState("");
  const [json, setJson] = useState();

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

  return (
    <>
      <div className="upload-container">
        <UpdateGraph onUpdate={onUpdate} />
      </div>
      <h1>{test}</h1>
      <ForceGraph2D
        graphData={json}
        nodeAutoColorBy={"val"}
        linkLabel={"label"}
        linkDirectionalArrowLength={4}
        linkDirectionalArrowRelPos={1}
        minZoom={1}
        linkDirectionalParticleSpeed={0.005}
        linkDirectionalParticleWidth={1.5}
        linkDirectionalParticles={3}
        // linkCanvasObject={(link, ctx, globalScale) => {
        //   const label = link.label;
        //   const fontSize = 12 / globalScale;
        //   ctx.font = `${fontSize}px Sans-Serif`;
        //   const textWidth = ctx.measureText(label).width;
        //   const bckgDimensions = [textWidth, fontSize].map(
        //     (n) => n + fontSize * 0.2
        //   ); // some padding

        //   ctx.fillStyle = "rgba(255, 255, 255, 0.5)";
        //   ctx.fillRect(
        //     link.x - bckgDimensions[0] / 2,
        //     link.y - bckgDimensions[1] / 2,
        //     ...bckgDimensions
        //   );

        //   console.log(link.x, link.y);
        //   ctx.textAlign = "center";
        //   ctx.textBaseline = "middle";
        //   ctx.fillStyle = "rgba(255, 255, 255, 0)";
        //   ctx.fillText(label, link.x, link.y);

        //   link.__bckgDimensions = bckgDimensions; // to re-use in nodePointerAreaPaint
        // }}
        // linkCanvasObjectMode={() => "after"}
      />
    </>
  );
}

export default KnowledgeGraph;
