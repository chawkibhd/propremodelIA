"use client";

import Box from "@mui/material/Box";
import { Button, TextField, Typography, Chip, Alert } from "@mui/material";
import useHomeForm from "@/lib/hooks/use-home-forms";
import formatPrice from "@/lib/utils/format-price";


const SingleFeatureForm = () => {

    const { result, error, isLoading, handleSubmit } = useHomeForm()

  return (
    <form
      onSubmit={handleSubmit}
      style={{
        display: "flex",
        flexDirection: "column",
        gap: "1.5rem",
      }}
    >
      <Typography
        variant="h4"
        component="h1"
        color="primary"
        textAlign="center"
        gutterBottom
        sx={{ fontWeight: 600 }}
      >
        Predict Land&apos;s Price
      </Typography>

      <TextField
        id="land_input"
        name="superficie"
        label="Enter Land Superficie (m²)"
        variant="outlined"
        fullWidth
        required
      />

      <Button
        variant="contained"
        type="submit"
        size="large"
        fullWidth
        disabled={isLoading}
        sx={{
          padding: "1rem",
          fontSize: "1.2rem",
          backgroundColor: "#1976d2",
        }}
      >
        {isLoading ? "Predicting..." : "Predict"}
      </Button>

      {error && (
        <Alert severity="error" sx={{ fontSize: "1rem" }}>
          {error}
        </Alert>
      )}

      {result && (
        <Box
          sx={{
            display: "flex",
            flexDirection: "column",
            alignItems: "center",
            gap: 2,
          }}
        >
          <Typography
            variant="h6"
            component="span"
            color="textSecondary"
            sx={{ fontWeight: "bold" }}
          >
            Predicted Value:
          </Typography>
          <Chip
            label={`${formatPrice(result)} Dzd`}
            color="success"
            sx={{ fontSize: "1rem", padding: "0.5rem" }}
          />
        </Box>
      )}
    </form>
  )
}

export default SingleFeatureForm