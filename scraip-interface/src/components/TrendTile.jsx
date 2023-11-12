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
import axios from "axios";

import TrendModal from "./TrendModal";

const TrendTile = ({ trendData, removeTrend }) => {
  const { id, title, keywords, description, urls, summary, updated } = trendData;

  const onDelete = () => {
    console.log("delete");
    axios
      .delete(`http://127.0.0.1:5000/api/v1/trends/${id}/`)
      .then(function (response) {
        console.log("deleted");
        removeTrend(id);
      })
      .catch(function (error) {
        console.log(error);
      });
  }

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
            <h3>{title}</h3>
            <h5>Updated: {new Date(updated).toDateString()}</h5>
            <div
              style={{
                paddingTop: "1rem",
              }}
            >
              {summary}
            </div>
          </div>
        </TileAboveTheFoldContent>
        <TileBelowTheFoldContent>
          <div
            style={{
              height: "300px",
              width: "360px",
            }}
          >
            <h4>Query</h4>
            <p>{keywords[0]}</p>
            <br />
            <h4>Description</h4>
            <p>{description}</p>
            <br />
            <h4>Sites</h4>
            <OrderedList style={{ padding: "10px 10px 10px 30px" }}>
              {urls.map((website, index) => (
                <ListItem key={index}>
                  <Link href={website}>{website}</Link>
                </ListItem>
              ))}
            </OrderedList>
          </div>
          <div
            style={{
              display: "flex",
              width: "45%",
              justifyContent: "space-between",
            }}
          >
            <Button onClick={TrendModal}>Edit</Button>
            <Button onClick={onDelete} style={{ backgroundColor: "#D3D3D3", color: "black" }}>
              Delete
            </Button>
          </div>
        </TileBelowTheFoldContent>
      </ExpandableTile>
    </div>
  );
};

export default TrendTile;
