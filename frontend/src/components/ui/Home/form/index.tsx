"use client";

import Box from "@mui/material/Box";
import Button from "@mui/material/Button";
import SingleFeatureForm from "./single-form-details";
import MultiFeatureForm from "./multi-form-details";
import { useState } from "react";

const Form = () => {
  const [isSingleForm, setIsSingleForm] = useState(true); // State to toggle between forms

  return (
    <Box
      sx={{
        width: { xs: "100%", sm: "90%", md: "80%" },
        padding: 4,
        backgroundColor: "white",
        borderRadius: 2,
        boxShadow: 4,
        display: "flex",
        flexDirection: "column",
        gap: 3,
      }}
    >
      {/* Toggle Button */}
      <Button
        variant="outlined"
        onClick={() => setIsSingleForm(!isSingleForm)} // Toggle the form
        sx={{
          alignSelf: "center",
          padding: "0.5rem 2rem",
          fontSize: "1rem",
          fontWeight: "bold",
        }}
      >
        {isSingleForm ? "Switch to Multi-Feature Form" : "Switch to Single-Feature Form"}
      </Button>

      {/* Render the selected form */}
      {isSingleForm ? <SingleFeatureForm /> : <MultiFeatureForm />}
    </Box>
  );
};

export default Form;
