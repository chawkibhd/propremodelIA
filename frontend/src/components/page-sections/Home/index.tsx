import Form from "@/components/ui/Home/form";
import Box from "@mui/material/Box";

const HomePage = () => {
  return (
    <Box
      sx={{
        display: "flex",
        width: { xs: "100%", sm: "90%", md: "40%" },
        justifyContent: "center",
        alignItems: "center",
        minHeight: "100vh",
        backgroundColor: "rgba(255, 255, 255, 0.6)",
        padding: 4,
      }}
    >
      <Form />
    </Box>
  );
};

export default HomePage;