// src/main.tsx
import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import './index.css';

// Mengidentifikasi elemen div dengan id 'root' pada index.html
const rootElement = document.getElementById('root');
if (!rootElement) {
  throw new Error("Elemen dengan id 'root' tidak ditemukan.");
}

// Membuat root React DOM dan merender komponen utama <App />
ReactDOM.createRoot(rootElement).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
