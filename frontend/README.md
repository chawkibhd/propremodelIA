# Frontend README

## Overview

The frontend is a **React-based application** powered by **Next.js** that provides users with an interactive, modern, and responsive interface for predicting land prices. It integrates seamlessly with the backend to support both single-feature and multi-feature regression predictions.

---

## Project Structure

```plaintext
frontend/
├── app/                     # Core Next.js app configuration and layout
│   ├── favicon.ico          # Application favicon
│   ├── globals.css          # Global CSS styles
│   ├── layout.tsx           # Global layout component
│   ├── page.tsx             # Main entry point for the application
│
├── components/              # Reusable UI components and layout
│   ├── layout/Home/         # Layout components for the Home section
│   │   ├── index.tsx        # Home layout wrapper
│
├── page-sections/           # Sections for pages
│   ├── Home/                # Homepage logic and layout
│   │   ├── index.tsx        # Homepage entry point
│
├── ui/                      # UI components for the Home page
│   ├── Home/form/           # Form-related components
│   │   ├── index.tsx        # Wrapper for forms
│   │   ├── multi-form-details.tsx  # Multi-feature prediction form
│   │   ├── single-form-details.tsx # Single-feature prediction form
│
├── lib/                     # Utility libraries and hooks
│   ├── Action/              # API call logic
│   │   ├── model.ts         # Functions for API requests (single and multi-feature)
│   ├── hooks/               # Custom React hooks
│   │   ├── use-home-forms.ts # Hook for form submission logic
│   ├── utils/               # Utility functions
│       ├── format-price.ts  # Formats predicted prices for display
│
├── public/                  # Static assets
├── styles/                  # Styles specific to the project (if any)
├── package.json             # Project dependencies and scripts
├── tsconfig.json            # TypeScript configuration
├── README.md                # Frontend documentation
```

---

## Key Features

### **1. Dynamic Forms**
- **Single-Feature Form**:
  - Users can input `superficie` for predictions using the single-feature regression model.
  - Component: `single-form-details.tsx`.
- **Multi-Feature Form**:
  - Users can input `superficie` and select `secteur` (dropdown: `"campagne"` or `"ville"`) for predictions using the multi-feature regression model.
  - Component: `multi-form-details.tsx`.

### **2. Toggle Between Forms**
- The user can toggle between the single-feature and multi-feature forms dynamically with a button.
- Component: `form/index.tsx`.

### **3. Real-Time API Integration**
- Communicates with the backend's endpoints:
  - `/predict-single`: Single-feature predictions.
  - `/predict-multi`: Multi-feature predictions.

### **4. Responsive Design**
- Built with **Material-UI** components for responsiveness and a clean, modern interface.

---

## Installation and Setup

### Prerequisites
- Ensure you have **Node.js 14+** and **npm** or **yarn** installed.

### Steps
1. Clone the repository and navigate to the `frontend/` directory:
   ```bash
   cd frontend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start the development server:
   ```bash
   npm run dev
   ```
4. Open the application in your browser:
   ```
   http://localhost:3000
   ```

---

## Forms Explained

### **1. Single-Feature Form**
- Input:
  - A single field for `superficie`.
- API Endpoint: `/predict-single`.
- Component: `ui/Home/form/single-form-details.tsx`.

#### Example Request:
```json
{
  "superficie": 120.5
}
```

#### Example Response:
```json
{
  "predicted_price": 2500000.0
}
```

---

### **2. Multi-Feature Form**
- Inputs:
  - `superficie`: Numeric input.
  - `secteur`: Dropdown with options (`campagne`, `ville`).
- API Endpoint: `/predict-multi`.
- Component: `ui/Home/form/multi-form-details.tsx`.

#### Example Request:
```json
{
  "superficie": 120.5,
  "secteur": "ville"
}
```

#### Example Response:
```json
{
  "predicted_price": 3000000.0
}
```

---

## Components

### **1. `Form`**
- Location: `ui/Home/form/index.tsx`.
- Dynamically toggles between the single-feature and multi-feature forms.
- Uses Material-UI's `Button` component for toggling.

### **2. `SingleFeatureForm`**
- Location: `ui/Home/form/single-form-details.tsx`.
- Handles single-feature predictions.

### **3. `MultiFeatureForm`**
- Location: `ui/Home/form/multi-form-details.tsx`.
- Handles multi-feature predictions.

### **4. API Integration**
- Location: `lib/Action/model.ts`.
- Functions:
  - `getModelRespond_Single`: Sends requests to `/predict-single`.
  - `getModelRespond_Multi`: Sends requests to `/predict-multi`.

---

## Utility Functions

### **1. `formatPrice`**
- Location: `lib/utils/format-price.ts`.
- Formats the predicted price to a readable currency format (DZD).

#### Example Usage:
```typescript
formatPrice(2500000); // Output: "2,500,000"
```