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
            flexDirection: "column",
            overflowY: "auto",
            alignItems: "start",
            maxWidth: "800px",
            width: "auto",
            margin: "auto",
            height: "80vh",
          }}
        >
          {queries.length === 0 && (
            <div
              ref={containerRef}
              style={{
                display: "flex",
                overflowY: "auto",
                alignItems: "center",
                maxWidth: "800px",
                width: "auto",
                margin: "auto",
                height: "80vh",
              }}
            >
              <div style={{ display: "flex", alignItems: "center" }}>
                <svg
                  enable-background="new 0 0 20 20"
                  height="100"
                  viewBox="0 0 20 20"
                  width="100"
                  xmlns="http://www.w3.org/2000/svg"
                >
                  <path d="m0 0h20v20h-20z" fill="none" />
                  <path d="m12.5 8 .79-1.72 1.71-.78-1.71-.78-.79-1.72-.76 1.72-1.74.78 1.74.78z" />
                  <path d="m4 10 .4-1.6 1.6-.4-1.6-.4-.4-1.6-.4 1.6-1.6.4 1.6.4z" />
                  <path d="m16.5 6c-1.07 0-1.84 1.12-1.35 2.14l-3.01 3.01c-.52-.25-.99-.14-1.29 0l-1.01-1.01c.1-.19.16-.41.16-.64 0-.83-.67-1.5-1.5-1.5s-1.5.67-1.5 1.5c0 .23.06.45.15.64l-3.01 3.01c-.19-.09-.41-.15-.64-.15-.83 0-1.5.67-1.5 1.5s.67 1.5 1.5 1.5 1.5-.67 1.5-1.5c0-.23-.06-.45-.15-.64l3.01-3.01c.52.25.99.14 1.29 0l1.01 1.01c-.1.19-.16.41-.16.64 0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5c0-.23-.06-.45-.15-.64l3.01-3.01c1.03.5 2.14-.29 2.14-1.35 0-.83-.67-1.5-1.5-1.5z" />
                </svg>
                <h3 style={{ alignContent: "center", paddingLeft: "20px" }}>
                  Search trends
                </h3>
              </div>
            </div>
          )}
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
                  <p style={{ margin: "20px", marginBottom: "40px" }}>
                    THIS IS WHERE THE RESPONSE COMES
                  </p>
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
