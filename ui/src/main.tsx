import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import "./index.css";
import Root from "./root"; // <- import Root instead of App

createRoot(document.getElementById("root")!).render(
  <StrictMode>
    <Root />   {/* <- render Root here */}
  </StrictMode>
);




/*import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.tsx'

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <App />
  </StrictMode>,
)
*/