import React from "react";
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableRow,
  Paper,
  Typography,
} from "@mui/material";

function DataTable({ rows }) {
  return (
    <Paper sx={{ mt: 4 }}>
      <Typography variant="h6" sx={{ p: 2 }}>
        📊 Claims Data
      </Typography>
      <Table>
        <TableHead>
          <TableRow>
            <TableCell><b>Name</b></TableCell>
            <TableCell><b>Village</b></TableCell>
            <TableCell><b>Type</b></TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {rows.length === 0 ? (
            <TableRow>
              <TableCell colSpan={3} align="center" sx={{ py: 3 }}>
                ⚠ No claims available
              </TableCell>
            </TableRow>
          ) : (
            rows.map((row, index) => (
              <TableRow key={index}>
                <TableCell>{row.name}</TableCell>
                <TableCell>{row.village}</TableCell>
                <TableCell>{row.type}</TableCell>
              </TableRow>
            ))
          )}
        </TableBody>
      </Table>
    </Paper>
  );
}

export default DataTable;
