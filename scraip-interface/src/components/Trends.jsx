import React from "react";
import { Grid, Row, Column } from "@carbon/react";
import { Button, Header, HeaderName, Heading } from "@carbon/react";

import CardModal from "./CardModal"; // Adjust the path as per your project structure

const Trends = () => {
  return (
    <>
      <Heading> Trends </Heading>
      <CardModal />
    </>
  );
};

export default Trends;
