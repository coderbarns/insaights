

import React, { useState } from 'react';
import './App.scss';
import { Button, Header, HeaderName, Heading } from "@carbon/react";
import Trends from './components/Trends'; // Assuming this is the path to your Trends component
import Insights from './components/Insights'; // Assuming this is the path to your Insights component

function App() {
  const [activeHeader, setActiveHeader] = useState('Trends');

  const renderComponent = () => {
    switch (activeHeader) {
      case 'Trends':
        return <Trends />;
      case 'Insights':
        return <Insights />;
      default:
        return null;
    }
  };

  return (
    <>
      <div
        style={{
          display: "flex",
          flexDirection: "column",
          minHeight: "100vh",
          padding: "20px",
        }}
      >
        <div style={{display: 'flex', marginBottom: '40px'}} aria-label="Header for Our Skeleton App">
          <p style={{fontWeight: 'bold', marginRight: '25px'}}>SCRAIP </p>
          <HeaderName href="#" prefix="" onClick={() => setActiveHeader('Trends')}>
            Trends
          </HeaderName>
          <HeaderName href="#" prefix="" onClick={() => setActiveHeader('Insights')}>
            Insights
          </HeaderName>
        </div>
        <div style={{ display: 'flex', width: '', justifyContent: 'space-around', }}>
          {renderComponent()}
        </div>
      </div>
    </>

  );
}

export default App;
