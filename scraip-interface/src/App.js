

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
        <div style={{display: 'flex', marginBottom: '40px', alignItems: "flex-end"}} aria-label="Header for Our Skeleton App">
          <h4 style={{fontWeight: 'bold', marginRight: '25px'}}>Insaights |</h4>
          <div>
            <HeaderName href="#" prefix="" onClick={() => setActiveHeader('Trends')}>
              Trends
            </HeaderName>
          </div>
          <div>
            <HeaderName href="#" prefix="" onClick={() => setActiveHeader('Insights')}>
              Insights
            </HeaderName>
          </div>
        </div>
        <div style={{width: '100%'}}>
          {renderComponent()}
        </div>
      </div>
    </>

  );
}

export default App;
