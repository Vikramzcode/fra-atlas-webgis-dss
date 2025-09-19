// frontend/src/components/ClaimForm.jsx

import React, { useState } from "react";
import { Box, TextField, Button, Typography } from "@mui/material";

// We pass a function `onAddClaim` from the parent page to this component
function ClaimForm({ onAddClaim }) {
  // This state will hold the data the user types into the form
  const [formData, setFormData] = useState({
    name: "",
    village: "",
    claimType: "IFR", // Default value
    status: "Pending", // Default value
  });

  // This function updates the state whenever the user types in an input field
  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prevData) => ({ ...prevData, [name]: value }));
  };

  // This function runs when the user clicks the "Submit" button
  const handleSubmit = (e) => {
    e.preventDefault(); // Prevents the page from reloading
    if (!formData.name || !formData.village) {
      alert("Please fill in all fields!");
      return;
    }
    onAddClaim(formData); // This sends the new claim data to the parent page
    // Clear the form after submission
    setFormData({ name: "", village: "", claimType: "IFR", status: "Pending" });
  };

  return (
    <Box
      component="form"
      onSubmit={handleSubmit}
      sx={{
        display: "flex",
        flexDirection: "column",
        gap: 2, // Adds space between form fields
        border: "1px solid #ccc",
        padding: 3,
        borderRadius: 2,
        marginBottom: 4,
      }}
    >
      <Typography variant="h6">📝 Add New FRA Claim</Typography>
      <TextField
        label="Patta Holder Name"
        name="name"
        value={formData.name}
        onChange={handleChange}
        required
      />
      <TextField
        label="Village Name"
        name="village"
        value={formData.village}
        onChange={handleChange}
        required
      />
      {/* In a real app, this might be a dropdown/select */}
      <TextField
        label="Claim Type (e.g., IFR, CR, CFR)"
        name="claimType"
        value={formData.claimType}
        onChange={handleChange}
      />
      <Button type="submit" variant="contained" color="primary">
        Add Claim
      </Button>
    </Box>
  );
}

export default ClaimForm;