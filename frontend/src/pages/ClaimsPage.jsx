// frontend/src/pages/ClaimsPage.jsx

import React, { useState, useEffect } from "react";
import {
  Container,
  Typography,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Paper,
} from "@mui/material";
import ClaimForm from "../components/ClaimForm"; // 👈 Import our new form
import { getClaims, addClaim } from "../services/api"; // 👈 Import our API functions

// Let's use some fake data for now, so we can see our table!
const DUMMY_CLAIMS = [
  { id: 1, name: "Rani Devi", village: "Shivpuri", claimType: "IFR", status: "Approved" },
  { id: 2, name: "Mohan Singh", village: "Kolaras", claimType: "CFR", status: "Pending" },
];

function ClaimsPage() {
  // This state will hold the list of all claims
  const [claims, setClaims] = useState(DUMMY_CLAIMS);

  // This comment block shows how you would fetch data from the REAL backend.
  // We will use this later when the backend is ready.
  /*
  useEffect(() => {
    getClaims()
      .then(response => {
        setClaims(response.data);
      })
      .catch(error => {
        console.error("Failed to fetch claims:", error);
      });
  }, []);
  */

  // This function will be passed to our ClaimForm component
  const handleAddClaim = (newClaimData) => {
    console.log("Adding new claim:", newClaimData);
    
    // This is how we would send the new claim to the backend
    /*
    addClaim(newClaimData)
      .then(response => {
        // Add the new claim returned from the API to our list
        setClaims(prevClaims => [...prevClaims, response.data]);
      })
      .catch(error => {
        console.error("Failed to add claim:", error);
      });
    */

    // For now, let's just add it to our dummy list
    const newClaim = { ...newClaimData, id: claims.length + 1 };
    setClaims(prevClaims => [...prevClaims, newClaim]);
  };

  return (
    <Container maxWidth="lg" sx={{ mt: 5 }}>
      <Typography variant="h4" gutterBottom>
        📋 FRA Claims Management
      </Typography>

      {/* This is our form component */}
      <ClaimForm onAddClaim={handleAddClaim} />

      {/* This is the table to display the claims */}
      <TableContainer component={Paper}>
        <Table>
          <TableHead sx={{ backgroundColor: "#f5f5f5" }}>
            <TableRow>
              <TableCell>ID</TableCell>
              <TableCell>Patta Holder Name</TableCell>
              <TableCell>Village</TableCell>
              <TableCell>Claim Type</TableCell>
              <TableCell>Status</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {claims.map((claim) => (
              <TableRow key={claim.id}>
                <TableCell>{claim.id}</TableCell>
                <TableCell>{claim.name}</TableCell>
                <TableCell>{claim.village}</TableCell>
                <TableCell>{claim.claimType}</TableCell>
                <TableCell>{claim.status}</TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>
    </Container>
  );
}

export default ClaimsPage;