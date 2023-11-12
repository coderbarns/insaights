import React, { useState, useEffect } from "react";
import TrendModal, { initalModalData } from "./TrendModal"; // Import your TrendModal
import TrendTile from "./TrendTile"; // Import your TrendTile

import { Heading, Button } from "@carbon/react";
import axios from "axios";

const TrendsDashboard = () => {
  const [trends, setTrends] = useState([]); // Array to hold trend data
  const [modalData, setModalData] = useState(initalModalData);
  const [showTrendModal, setShowTrendModal] = useState(false); // State to control modal open/close

  const handleNewTrend = (newTrend) => {
    const existingTrendIndex = trends.findIndex(t => t.id === newTrend.id)
    if (existingTrendIndex !== -1) {
      console.log('is update')
      console.log(trends)
      var newTrends = [...trends]
      newTrends.splice(existingTrendIndex, 1, newTrend)
      setTrends(newTrends)
    } else {
      console.log('is create')
      setTrends([...trends, newTrend]);
    }
    setModalData(initalModalData);
    setShowTrendModal(false);
  };

  const removeTrend = (id) => {
    setTrends(trends.filter((trend) => trend.id !== id));
  }

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get("http://127.0.0.1:5000/api/v1/trends/");
        if (response.data) {
          setTrends(response.data);
        }
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    };

    fetchData();
  }, []);

  const onClose = () => {
    setShowTrendModal(false);
    setModalData(initalModalData);
  }

  const onEdit = (trend) => () => {
    setShowTrendModal(true);
    console.log(trend)
    setModalData(trend);
  }

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
          <Button onClick={() => setShowTrendModal(true)}>
            Add Trend
          </Button>

          <TrendModal showTrendModal={showTrendModal} onSubmit={handleNewTrend} modalData={modalData} onClose={onClose} setModalData={setModalData} />
        </div>
      </div>
      <div
        className="responsive-grid"
        style={{
          display: "grid",
          gridTemplateColumns: "repeat(2, 1fr)", // Creates two columns
          gap: "20px", // Adjust the gap between tiles as needed
          justifyContent: "center", // Center the grid itself
          alignItems: "start", // Align items to the start of each cell
          maxWidth: "1200px", // Adjust based on the size of your tiles
          margin: "auto", // Center the grid container
        }}
      >
        {trends.map((trend, index) => (
          <TrendTile key={index} trendData={trend} removeTrend={removeTrend} onEdit={onEdit(trend)} />
        ))}
      </div>
    </>
  );
};

export default TrendsDashboard;
