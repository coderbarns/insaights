import {
  ExpandableTile,
  TileAboveTheFoldContent,
  TileBelowTheFoldContent,
  Button,
  TextInput,
  OrderedList,
  ListItem,
  Link,
} from "@carbon/react";

import TrendModal from "./TrendModal";

const TrendTile = ({ trendData }) => {
  const { browserQuery, description, urls, summary } = trendData;

  return (
    <div
      style={{
        width: "400px",
      }}
    >
      <ExpandableTile
        style={{ width: "590px" }}
        onClick={() => console.log("click")}
        id="expandable-tile-1"
        tileCollapsedIconText="Interact to Expand tile"
        tileExpandedIconText="Interact to Collapse tile"
      >
        <TileAboveTheFoldContent>
          <div
            style={{
              height: "300px",
              width: "fit-content",
            }}
          >
            <h3>{browserQuery}</h3>
            <div
              style={{
                paddingTop: "1rem",
              }}
            >
              {summary}
            </div>
            {description}
          </div>
        </TileAboveTheFoldContent>
        <TileBelowTheFoldContent>
          <div
            style={{
              height: "300px",
              width: "360px",
            }}
          >
            <h5>Relevant links</h5>
            <OrderedList style={{ padding: "10px 10px 10px 30px" }}>
              {urls.map((website, index) => (
                <ListItem key={index}>
                  <Link href={website}>{website}</Link>
                </ListItem>
              ))}
            </OrderedList>
            <h4>summary</h4>
          </div>
          <div
            style={{
              display: "flex",
              width: "45%",
              justifyContent: "space-between",
            }}
          >
            <Button onClick={TrendModal}>Edit</Button>
            <Button style={{ backgroundColor: "#D3D3D3", color: "black" }}>
              Delete
            </Button>
          </div>
        </TileBelowTheFoldContent>
      </ExpandableTile>
    </div>
  );
};

export default TrendTile;
