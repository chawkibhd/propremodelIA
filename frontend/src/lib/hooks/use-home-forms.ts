"use client";

import { useState } from "react";
import { getModelRespond } from "../Action/model";

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
  
      if (!superficie || superficie.trim() === "") {
        setError("Please enter valid land details.");
        setIsLoading(false);
        return;
      }
  
      try {
        const data = await getModelRespond(formData);
        setResult(data?.predicted_price || "No value returned.");
      } catch (err: any) {
        setError(err.message || "Something went wrong while predicting the price.");
      } finally {
        setIsLoading(false); 
      }
    };

  return {
    result,
    error,
    isLoading,
    handleSubmit
  }
}

export default useHomeForm