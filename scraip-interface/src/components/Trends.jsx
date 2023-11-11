import React, { useState } from "react";
import TrendModal from "./TrendModal"; // Import your TrendModal
import TrendTile from "./TrendTile"; // Import your TrendTile

import { Heading } from "@carbon/react";

const TrendsDashboard = () => {
  const [trends, setTrends] = useState([]); // Array to hold trend data

  const handleNewTrend = (newTrend) => {
    setTrends([...trends, newTrend]);
  };

  return (
    <>
      <div
        style={{
          display: "flex",
          justifyContent: "space-between", // Center the grid itself
          alignItems: "start", // Align items to the start of each cell
          maxWidth: "1260px", // Adjust based on the size of your tiles
          margin: "auto",
          marginBottom: "40px",
        }}
      >
        <div style={{}}>
          <Heading>Trends</Heading>
        </div>
        <div>
          <TrendModal onNewTrend={handleNewTrend} />
        </div>
      </div>
      <div
        style={{
          display: "grid",
          gridTemplateColumns: "repeat(3, 1fr)", // Creates two columns
          gap: "20px", // Adjust the gap between tiles as needed
          justifyContent: "center", // Center the grid itself
          alignItems: "start", // Align items to the start of each cell
          maxWidth: "1200px", // Adjust based on the size of your tiles
          margin: "auto", // Center the grid container
        }}
      >
        {trends.map((trend, index) => (
          <TrendTile key={index} trendData={trend} />
        ))}
      </div>
    </>
  );
};

export default TrendsDashboard;
