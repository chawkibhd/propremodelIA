"use server";

export const getModelRespond = async (formData: FormData) => {
  const superficie = formData.get("superficie");

  if (!superficie) {
    throw new Error("Land details are required.");
  }

  try {
    const response = await fetch("http://127.0.0.1:8000/predict", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ superficie }), // Send data as JSON
    });

    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.message || "An unknown error occurred.");
    }

    const data = await response.json(); // Parse JSON response
    return data;
  } catch (error: unknown) {
    if (error instanceof Error) {
      throw new Error(error.message || "Network error occurred.");
  } else {
      throw new Error("An unknown error occurred.");
  }
  }
};
