import {
  ComposedModal,
  ModalBody,
  Button,
  TextInput,
  Select,
  SelectItem,
  TextArea,
  ProgressIndicator,
  ProgressStep,
} from "@carbon/react";
import ReactDOM from "react-dom";
import { useState, useRef } from "react";

const CardModal = () => {
  const addWebsite = (event) => {
    event.preventDefault();
    if (currentWebsite) {
      setWebsites([...websites, currentWebsite]);
      setCurrentWebsite("");
    }
  };

  const handleInputChange = (event) => {
    event.stopPropagation();
    setCurrentWebsite(event.target.value);
  };

  const [websites, setWebsites] = useState([]);
  const [currentWebsite, setCurrentWebsite] = useState("");
  const button = useRef();

  const ModalStateManager = ({
    renderLauncher: LauncherContent,
    children: ModalContent,
  }) => {
    const [open, setOpen] = useState(false);
    return (
      <>
        {!ModalContent || typeof document === "undefined"
          ? null
          : ReactDOM.createPortal(
              <ModalContent open={open} setOpen={setOpen} />,
              document.body
            )}
        {LauncherContent && <LauncherContent open={open} setOpen={setOpen} />}
      </>
    );
  };

  return (
    <ModalStateManager
      renderLauncher={({ setOpen }) => (
        <Button ref={button} onClick={() => setOpen(true)}>
          Add trend
        </Button>
      )}
    >
      {({ open, setOpen }) => (
        <ComposedModal
          launcherButtonRef={button}
          modalHeading="Add a custom domain"
          modalLabel="Account resources"
          primaryButtonText="Add"
          secondaryButtonText="Cancel"
          open={open}
          preventCloseOnClickOutside={false}
          style={{ padding: "20px" }}
        >
          <ModalBody hasForm>
            <ProgressIndicator
              style={{
                marginBottom: "4rem",
              }}
            >
              <ProgressStep
                complete
                label="Add query"
                description="Step 1: Getting started with Carbon Design System"
                secondaryLabel="Optional label"
              />
              <ProgressStep
                current
                label="Add description"
                description="Step 2: Getting started with Carbon Design System"
              />
              <ProgressStep
                label="Third step with tooltip"
                description="Step 3: Getting started with Carbon Design System"
              />
              <ProgressStep
                label="Fourth step"
                description="Step 4: Getting started with Carbon Design System"
                invalid
                secondaryLabel="Example invalid step"
              />
            </ProgressIndicator>
            <p
              style={{
                marginBottom: "1rem",
              }}
            >
              Create a Trend to get the latest insights relevant for your
              business
            </p>
            <TextInput
              data-modal-primary-focus
              id="text-input-1"
              labelText="Browser query"
              placeholder="Environmental catastrophies"
              style={{
                marginBottom: "1rem",
              }}
            />
            <TextArea
              data-modal-primary-focus
              id="text-input-1"
              labelText="Description"
              placeholder="e.g. environmental catastrophies that are affecting energy production and pricing."
              style={{
                marginBottom: "1rem",
              }}
            />
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

            <Button onClick={() => setOpen(false)}>Set Trend</Button>
          </ModalBody>
        </ComposedModal>
      )}
    </ModalStateManager>
  );
};

export default CardModal;
