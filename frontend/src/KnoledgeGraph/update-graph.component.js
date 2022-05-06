import React from "react";

function UpdateGraph({ onUpdate }) {
  return (
    <div className="upload-container">
      <button className="upload-container" onClick={onUpdate}>
        Update
      </button>
    </div>
  );
}

export default UpdateGraph;
