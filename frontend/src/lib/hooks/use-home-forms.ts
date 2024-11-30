"use client";

import { useState } from "react";
import { getModelRespond_Single, getModelRespond_Multi } from "../Action/model";

const useHomeForm = () => {
  const [result, setResult] = useState<string>("");
  const [error, setError] = useState<string>("");
  const [isLoading, setIsLoading] = useState<boolean>(false);

  const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    setResult("");
    setError("");
    setIsLoading(true);

    const formData = new FormData(event.currentTarget);
    const superficie = formData.get("superficie")?.toString();
    const secteur = formData.get("secteur")?.toString(); // Get 'secteur' for multi-feature model

    if (!superficie || superficie.trim() === "") {
      setError("Please enter valid land details.");
      setIsLoading(false);
      return;
    }

    try {
      let data;

      if (secteur && secteur.trim() !== "") {
        // Use multi-feature prediction if 'secteur' is provided
        data = await getModelRespond_Multi(formData);
      } else {
        // Use single-feature prediction if only 'superficie' is provided
        data = await getModelRespond_Single(formData);
      }

      setResult(data?.predicted_price || "No value returned.");
    } catch (err: unknown) {
      if (err instanceof Error) {
        setError(
          err.message || "Something went wrong while predicting the price.",
        );
      } else {
        setError("An unknown error occurred.");
      }
    } finally {
      setIsLoading(false);
    }
  };

  return {
    result,
    error,
    isLoading,
    handleSubmit,
  };
};

export default useHomeForm;
