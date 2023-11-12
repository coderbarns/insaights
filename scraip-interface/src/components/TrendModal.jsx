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

import axios from "axios";

export const initalModalData = {
  id: null,
  keywords: "",
  description: "",
  urls: [],
  currentWebsite: "",
  title: "",
  scrape_interval: "",
}

function TrendModal({ showTrendModal, onSubmit, onClose, modalData, setModalData }) {
  const { id, title, keywords, description, scrape_interval, urls } = modalData;

  const addWebsite = (event) => {
    event.preventDefault();
    if (modalData.currentWebsite) {
      setModalData({ ...modalData, urls: [...urls, modalData.currentWebsite], currentWebsite: "" });
    }
  };

  const handleInputChange = (event) => {
    setModalData({ ...modalData, currentWebsite: event.target.value });
  };

  const handleSubmit = () => {
    var data = {
      title: title,
      description: description,
      keywords: [keywords],
      urls: urls,
      scrape_interval: scrape_interval,
      summary: "Overwiew is being generated.",
      updated: new Date().toJSON(), // not used
    }
    var method;
    var url
    if (id) {
      method = axios.put;
      url = `http://127.0.0.1:5000/api/v1/trends/${id}`
    } else {
      method = axios.post;
      url = "http://127.0.0.1:5000/api/v1/trends"
      data['id'] = id;
    }
    method(url, {
      title: title,
      description: description,
      keywords: [keywords],
      urls: urls,
      scrape_interval: scrape_interval,
      summary: "Overwiew is being generated.",
      updated: new Date().toJSON(), // not used
    })
      .then(function (response) {
        console.log(response);
        onSubmit();
      })
      .catch(function (error) {
        console.log(error);
      });
  };

  return (
    <>
      <ComposedModal
        open={showTrendModal}
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
              current={urls.length > 0}
              label="Title"
              secondaryLabel="Name your module"
            />
            <ProgressStep
              complete={keywords !== ""}
              label="Add query"
              secondaryLabel="Add your search query"
            />
            <ProgressStep
              complete={description !== ""}
              current={keywords !== "" && description === ""}
              label="Add description"
              secondaryLabel="Describe your wanted results"
            />
            <ProgressStep
              complete={urls.length > 0}
              current={description !== "" && urls.length === 0}
              label="Add sites"
              secondaryLabel="Add relevant sites to your search"
            />
            <ProgressStep
              current={urls.length > 0}
              label="Save Trend"
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
            placeholder="Name for your Trend"
            value={title}
            onChange={(e) => setModalData({ ...modalData, title: e.target.value })}
            style={{
              marginBottom: "1rem",
            }}
          />
          <TextInput
            data-modal-primary-focus
            id="text-input-1"
            labelText="Search query"
            placeholder="e.g. Environmental catastrophies in Europe"
            value={keywords}
            onChange={(e) => setModalData({ ...modalData, keywords: [e.target.value] })}
            style={{
              marginBottom: "1rem",
            }}
          />
          <TextArea
            data-modal-primary-focus
            id="text-input-1"
            labelText="Description"
            placeholder="Describe your wanted results (e.g. How are environmental catastrophies affecting energy production and pricing?)"
            value={description}
            onChange={(e) => setModalData({ ...modalData, description: e.target.value })}
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
            value={scrape_interval}
            onChange={(e) => setModalData({ ...modalData, scrape_interval: e.target.value })}
          >
            <SelectItem value={"daily"} text="Once a day" />
            <SelectItem value={"weekly"} text="Once a week" />
            <SelectItem value={"monthly"} text="Once a month" />
          </Select>
          <TextInput
            data-modal-primary-focus
            value={modalData.currentWebsite}
            onChange={handleInputChange}
            id="website-input"
            labelText="Relevant urls"
            placeholder="example.com"
            style={{
              marginBottom: "1rem",
            }}
          />
          <Button onClick={addWebsite}>Add Website</Button>

          {urls.length > 0 && (
            <div style={{ marginTop: "1rem" }}>
              <p>Added Websites:</p>
              <ul>
                {urls.map((website, index) => (
                  <li key={index}>{website}</li>
                ))}
              </ul>
            </div>
          )}
        </ModalBody>
        <ModalFooter>
          <Button
            style={{ backgroundColor: "#D3D3D3", color: "black" }}
            onClick={() => onClose()}
          >
            Close
          </Button>
          <Button style={{}} onClick={() => handleSubmit()}>
            Save Trend
          </Button>
        </ModalFooter>
      </ComposedModal>
    </>
  );
}

export default TrendModal;
