"use server";

export const getModelRespond_Single = async (formData: FormData) => {
  const superficie = formData.get("superficie");

  if (!superficie) {
    throw new Error("Land details are required.");
  }

  try {
    const response = await fetch("http://127.0.0.1:8000/predict-single", {
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


export const getModelRespond_Multi = async (formData: FormData) => {
  const superficie = formData.get("superficie");
  const secteurText = formData.get("secteur"); // Get secteur as text (e.g., "campagne")

  if (!superficie || !secteurText) {
    throw new Error("Both 'superficie' and 'secteur' details are required.");
  }

  // Map secteur to encoded values
  const secteurEncoding: Record<string, number> = {
    campagne: 0,
    ville: 1,
  };

  // Get the encoded value for secteur
  const secteur = secteurEncoding[secteurText as string];
  if (secteur === undefined) {
    throw new Error(`Invalid secteur value: ${secteurText}`);
  }

  try {
    const response = await fetch("http://127.0.0.1:8000/predict-multi", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        superficie: parseFloat(superficie as string), // Convert superficie to a number
        secteur: secteur,                             // Use the encoded value
      }),
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
