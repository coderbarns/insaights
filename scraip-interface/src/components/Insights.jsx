// import TrendModal from "./TrendModal";
import { Button, Heading, Search } from "@carbon/react";
import axios from "axios";
import { useState } from "react";
import React, { useEffect, useRef } from "react";

function uuidv4() {
  return "10000000-1000-4000-8000-100000000000".replace(/[018]/g, (c) =>
    (
      c ^
      (crypto.getRandomValues(new Uint8Array(1))[0] & (15 >> (c / 4)))
    ).toString(16)
  );
}

const Insights = () => {
  const [conversationId, setConversationId] = useState([]);
  const [data, setData] = useState({ messages: [], documents: [] });
  const [currentInput, setCurrentInput] = useState("");
  const [loading, setLoading] = useState(false);
  const containerRef = useRef(null);

  const addQuery = () => {
    if (currentInput) {
      setLoading(true);

      axios
        .post("http://localhost:5000/api/v1/documents/search/", {
          conversation_id: conversationId,
          query: currentInput,
        })
        .then(function (response) {
          console.log(response);
          setData(response.data);
          setCurrentInput("");
          setLoading(false);
        })
        .catch(function (error) {
          console.log(error);
          setLoading(false);
        });
    }
  };

  const scrollToBottom = () => {
    if (containerRef.current) {
      containerRef.current.scrollTop = containerRef.current.scrollHeight;
    }
  };

  useEffect(() => {
    if (containerRef.current) {
      const isScrolledToBottom =
        containerRef.current.scrollHeight - containerRef.current.clientHeight <=
        containerRef.current.scrollTop + 1;

      if (isScrolledToBottom) {
        scrollToBottom();
      }
    }
  }, [data]);

  useEffect(() => {
    setConversationId(uuidv4());
  }, []);

  return (
    <div>
      <div style={{ display: "flex", maxWidth: "1260px", margin: "auto" }}>
        <Heading>Insights</Heading>
      </div>
      <div
        style={{
          display: "flex",
          flexDirection: "column",
          overflowY: "auto",
          maxWidth: "800px",
          margin: "auto",
          height: "75vh",
        }}
      >
        {data.messages.length === 0 && (
          <div
            style={{
              display: "flex",
              justifyContent: "center",
              alignItems: "center",
              height: "75vh",
            }}
          >
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
            <h3 style={{ paddingLeft: "20px" }}>
              Discover patterns from your data modules
            </h3>
          </div>
        )}

        {data.messages.length > 0 && (
          <div ref={containerRef} style={{ width: "100%" }}>
            {data.messages
              .filter((v) => v.role == "assistant" || v.role == "user")
              .map((message, index) => (
                <div key={index}>
                  <h4 style={{ fontWeight: "bold", margin: "20px" }}>
                    {message.role}
                  </h4>
                  <p style={{ margin: "20px", marginBottom: "40px" }}>
                    {message.content}
                  </p>
                </div>
              ))}
          </div>
        )}
      </div>
      <div
        style={{
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
          marginTop: "auto",
        }}
      >
        <div>
          <Search
            style={{ minWidth: "800px", maxWidth: "800px" }}
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
          <Button onClick={addQuery} disabled={loading}>
            {loading ? "Loading..." : "Find Insights"}
          </Button>
        </div>
      </div>
      <p
        style={{
          margin: "auto",
          textAlign: "center",
          padding: "4px",
          fontSize: "12px",
        }}
      >
        Search for insights based on your trend modules.
      </p>
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
