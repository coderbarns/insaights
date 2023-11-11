import CardModal from "./TrendModal";
import { Button, Header, HeaderName, Heading } from "@carbon/react";

const Insights = () => {
  return (
    <div
      style={{
        display: "flex",
        justifyContent: "space-between", // Center the grid itself
        alignItems: "start", // Align items to the start of each cell
        maxWidth: "1260px", // Adjust based on the size of your tiles
        margin: "auto",
      }}
    >
      <Heading> Insights </Heading>
      <div
        style={{
          display: "flex",
          flexDirection: "column",
          justifyContent: "center",
          alignItems: "center",
          height: "100vh",
        }}
      ></div>
    </div>
  );
};

export default Insights;
