// import TrendModal from "./TrendModal";
import {
  Button,
  Header,
  HeaderName,
  Heading,
  Search,
  TreeView,
  TreeNode,
} from "@carbon/react";

import { useState } from "react";
import React, { useEffect, useRef } from "react";

const Insights = () => {
  const [queries, setQueries] = useState([]);
  const [currentInput, setCurrentInput] = useState("");
  const containerRef = useRef(null);

  console.log(queries);

  const addQuery = () => {
    if (currentInput) {
      setQueries([...queries, currentInput]);
      setCurrentInput("");
    }
  };

  const scrollToBottom = () => {
    if (containerRef.current) {
      containerRef.current.scrollTop = containerRef.current.scrollHeight;
    }
  };

  // Scroll to bottom on new entries, but only if already at bottom
  useEffect(() => {
    if (containerRef.current) {
      const isScrolledToBottom =
        containerRef.current.scrollHeight - containerRef.current.clientHeight <=
        containerRef.current.scrollTop + 1;

      if (isScrolledToBottom) {
        scrollToBottom();
      }
    }
  }, [queries]);

  return (
    <div>
      <div
        style={{
          display: "flex",
          justifyContent: "space-between", // Center the grid itself
          maxWidth: "1260px", // Adjust based on the size of your tiles
          margin: "auto",
        }}
      >
        <div style={{}}>
          <Heading>Insights</Heading>
        </div>
      </div>

      <div>
        <div
          ref={containerRef}
          style={{
            display: "flex",
            flexDirection: "column-reverse",
            overflowY: "auto",
            alignItems: "start",
            maxWidth: "800px",
            width: "auto",
            margin: "auto",
            height: "80vh",
          }}
        >
          {queries.length > 0 && (
            <div
              style={{
                width: "100%",
                backgroundColor: "",
              }}
            >
              {queries.map((query, index) => (
                <>
                  <h4
                    style={{ fontWeight: "bold", margin: "20px" }}
                    key={index}
                  >
                    {query}
                  </h4>
                  <p>sdfsafadfasdfasd</p>
                </>
              ))}
            </div>
          )}
        </div>
        <div
          style={{
            display: "flex",
            justifyContent: "center",
            alignItems: "center",
            width: "auto",
            marginTop: "auto",
          }}
        >
          <div style={{ alignItems: "center" }}>
            <Search
              style={{
                minWidth: "800px",
                maxWidth: "800px",
                alignItems: "flex-end",
              }}
              size="lg"
              placeholder="Search all trends"
              value={currentInput}
              labelText="Search"
              closeButtonLabelText="Clear search input"
              id="search-1"
              onChange={(e) => setCurrentInput(e.target.value)}
            />
          </div>
          <div>
            <Button onClick={addQuery}>Find Insights</Button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Insights;

{
  /* <div>
<Heading style={{ paddingBottom: "20px" }}> Insights </Heading>
<TreeView style={{}} label="Recent events">
{renderTree(nodes)}
</TreeView>
</div> 

const renderTree = (nodes) => {
return nodes.map((node) => (
<TreeNode key={node.id} id={node.id} label={node.label}>
{node.children && renderTree(node.children)}
</TreeNode>
));
};
*/
}
