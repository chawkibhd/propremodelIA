import Box from "@mui/material/Box";
import FormDetails from "./form-details";


const Form = () => {
  return (
    <Box
    sx={{
      width: { xs: "100%", sm: "90%", md: "80%" },
      padding: 4,
      backgroundColor: "white",
      borderRadius: 2,
      boxShadow: 4,
    }}
  >
    <FormDetails />
  </Box>
  )
}

export default Form