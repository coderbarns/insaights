import {
  ComposedModal,
  ModalBody,
  Button,
  TextInput,
  TextArea,
  ProgressIndicator,
  ProgressStep,
  ModalFooter,
  Select,
  SelectItem,
} from "@carbon/react";

import { useState, useRef } from "react";

function TrendModal({ onNewTrend }) {
  const [open, setOpen] = useState(false);
  const [browserQuery, setBrowserQuery] = useState("");
  const [description, setDescription] = useState("");
  const [websites, setWebsites] = useState([]);
  const [currentWebsite, setCurrentWebsite] = useState("");
  const button = useRef();

  const addWebsite = (event) => {
    event.preventDefault();
    if (currentWebsite) {
      setWebsites([...websites, currentWebsite]);
      setCurrentWebsite("");
    }
  };

  const handleInputChange = (event) => {
    setCurrentWebsite(event.target.value);
  };

  const resetForm = () => {
    setBrowserQuery("");
    setDescription("");
    setCurrentWebsite("");
    setWebsites([]);
  };

  const handleSubmit = () => {
    const newTrend = {
      browserQuery,
      description,
      websites,
    };

    onNewTrend(newTrend);

    setBrowserQuery("");
    setDescription("");
    setCurrentWebsite("");
    setWebsites([]);

    handleSetOpen();
  };

  const handleSetOpen = (newOpen) => {
    if (!newOpen) {
      resetForm();
    }
    setOpen(newOpen);
  };

  return (
    <>
      <Button ref={button} onClick={() => setOpen(true)}>
        Add trend
      </Button>

      <ComposedModal
        open={open}
        preventCloseOnClickOutside={true}
        style={{ padding: "20px" }}
      >
        <ModalBody hasForm>
          <ProgressIndicator
            spaceEqually
            style={{
              marginTop: "1rem",
              marginBottom: "4rem",
            }}
          >
            <ProgressStep
              current={websites.length > 0}
              label="Title"
              secondaryLabel="Name your module"
            />
            <ProgressStep
              complete={browserQuery !== ""}
              label="Add query"
              secondaryLabel="Add your search query"
            />
            <ProgressStep
              complete={description !== ""}
              current={browserQuery !== "" && description === ""}
              label="Add description"
              secondaryLabel="Describe your wanted results"
            />
            <ProgressStep
              complete={websites.length > 0}
              current={description !== "" && websites.length === 0}
              label="Add sites"
              secondaryLabel="Add relevant sites to your search"
            />
            <ProgressStep
              current={websites.length > 0}
              label="Set Trend"
              secondaryLabel="Get your insights"
            />
          </ProgressIndicator>
          <p
            style={{
              marginBottom: "1rem",
            }}
          >
            Create a Trend to get the latest insights relevant for your business
          </p>
          <TextInput
            data-modal-primary-focus
            id="text-input-1"
            labelText="Title"
            placeholder="Name for your data module"
            value={browserQuery}
            onChange={(e) => setBrowserQuery(e.target.value)}
            style={{
              marginBottom: "1rem",
            }}
          />
          <TextInput
            data-modal-primary-focus
            id="text-input-1"
            labelText="Search query"
            placeholder="e.g. Environmental catastrophies in Europe"
            value={browserQuery}
            onChange={(e) => setBrowserQuery(e.target.value)}
            style={{
              marginBottom: "1rem",
            }}
          />
          <TextArea
            data-modal-primary-focus
            id="text-input-1"
            labelText="Description"
            placeholder="Describe your wanted results (e.g. how are environmental catastrophies affecting energy production and pricing.)"
            value={description}
            onChange={(e) => setDescription(e.target.value)}
            style={{
              marginBottom: "1rem",
            }}
          />
          <Select
            id={`select-1`}
            labelText="Frequency of the search"
            style={{
              marginBottom: "1rem",
            }}
          >
            <SelectItem value={1} text="Once a day" />
            <SelectItem value={2} text="Once a week" />
            <SelectItem value={3} text="Once a month" />
          </Select>
          <TextInput
            data-modal-primary-focus
            value={currentWebsite}
            onChange={handleInputChange}
            id="website-input"
            labelText="Relevant websites"
            placeholder="https://example.com"
            style={{
              marginBottom: "1rem",
            }}
          />
          <Button onClick={addWebsite}>Add Website</Button>

          {websites.length > 0 && (
            <div style={{ marginTop: "1rem" }}>
              <p>Added Websites:</p>
              <ul>
                {websites.map((website, index) => (
                  <li key={index}>{website}</li>
                ))}
              </ul>
            </div>
          )}
        </ModalBody>
        <ModalFooter>
          <Button
            style={{ backgroundColor: "#D3D3D3", color: "black" }}
            onClick={() => handleSetOpen()}
          >
            Close
          </Button>
          <Button style={{}} onClick={() => handleSubmit()}>
            Set Trend
          </Button>
        </ModalFooter>
      </ComposedModal>
    </>
  );
}

export default TrendModal;
