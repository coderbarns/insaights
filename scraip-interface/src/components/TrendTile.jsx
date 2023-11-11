import {
  ExpandableTile,
  TileAboveTheFoldContent,
  TileBelowTheFoldContent,
  Button,
  TextInput,
} from "@carbon/react";

const TrendTile = ({ trendData }) => {
  const { browserQuery, description, websites } = trendData;

  return (
    <div
      style={{
        width: "400px",
      }}
    >
      <ExpandableTile
        onClick={() => console.log("click")}
        id="expandable-tile-1"
        tileCollapsedIconText="Interact to Expand tile"
        tileExpandedIconText="Interact to Collapse tile"
      >
        <TileAboveTheFoldContent>
          <div
            style={{
              height: "200px",
              width: "360px",
            }}
          >
            <h5>{browserQuery}</h5>
            <div
              style={{
                paddingTop: "1rem",
              }}
            ></div>
            {description}
          </div>
        </TileAboveTheFoldContent>
        <TileBelowTheFoldContent>
          <div
            style={{
              height: "200px",
              width: "360px",
            }}
          >
            <h4>summary</h4>
          </div>
          <div
            style={{
              display: "flex",
              width: "65%",
              justifyContent: "space-between",
            }}
          >
            <Button>Edit</Button>
            <Button>Delete</Button>
          </div>
        </TileBelowTheFoldContent>
      </ExpandableTile>
    </div>
  );
};

export default TrendTile;
