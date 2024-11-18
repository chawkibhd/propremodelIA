import type { Metadata } from "next";
import "./globals.css";
import HomeLyout from "@/components/layout/Home";

export const metadata = {
  title: "Predict Land Price",
  description: "An application to predict land prices based on input details.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className={`antialiased`}>
        <HomeLyout>{children}</HomeLyout>
      </body>
    </html>
  );
}
