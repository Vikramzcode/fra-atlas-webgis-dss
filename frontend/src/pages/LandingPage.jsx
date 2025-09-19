import React from "react";
import { Button, Container, Typography, Box } from "@mui/material";
import { useNavigate } from "react-router-dom";
import Navbar from "../components/Navbar";


function LandingPage() {
  const navigate = useNavigate();

  return (
    <Container maxWidth="md" sx={{ textAlign: "center", mt: 10 }}>
      <Typography variant="h3" gutterBottom>
        🌳 FRA Atlas WebGIS DSS
      </Typography>
      <Typography variant="h6" color="text.secondary" gutterBottom>
        AI-powered system for monitoring and decision support in Forest Rights Act (FRA)
      </Typography>

      <Box sx={{ mt: 5 }}>
        <Button
          variant="contained"
          color="primary"
          size="large"
          onClick={() => navigate("/claims")}
        >
          🚀 Go to Claims Page
        </Button>
      </Box>
    </Container>
  );
}

export default LandingPage;
<>
  <Navbar />
  <Container maxWidth="md" sx={{ textAlign: "center", mt: 10 }}>
    {/* rest of your LandingPage content */}
  </Container>
</>

