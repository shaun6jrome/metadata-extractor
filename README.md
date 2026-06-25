# Metadata Extractor (EXIF Analyzer)
#INTERN ID - CITS4449

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-Framework-FF4B4B.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Build](https://img.shields.io/badge/build-passing-brightgreen)

**Live Demo:** [Metadata Extractor on Streamlit Community Cloud](https://metadata-extractor-iegf4ode5zcnplnssmf87k.streamlit.app/)

A comprehensive digital forensics tool built with Python and Streamlit to extract, analyze, and display embedded metadata from image files. Designed with a professional dark mode interface, this application is ideal for cybersecurity students, digital forensic investigators, photographers, and security researchers seeking to understand data exposure and privacy risks.

---

## 📖 Overview

In the digital forensics landscape, every image carries a digital fingerprint known as EXIF (Exchangeable Image File Format) data. This tool automates the extraction and parsing of these hidden artifacts. It safely processes images entirely in-memory and provides users with an intuitive dashboard breaking down technical camera settings, geographical locations, and potential privacy risks.

This project was developed as a comprehensive exercise in **Data Parsing, Geospatial Visualization, and Risk Analysis**, making it an excellent demonstration of full-stack Python capabilities for cybersecurity and data-driven applications.

---

## 🚀 Key Features

*   **Robust EXIF Extraction Engine**: Leverages both `ExifRead` and `Pillow` to reliably parse embedded metadata, including Camera Manufacturer, Model, Lens Info, Date Taken, ISO, Exposure Time, and Aperture.
*   **Geospatial Visualization**: Automatically detects raw GPS ratios from EXIF data, converts them into standard decimal degrees, and visually plots the exact geographical location on an interactive `Folium` map.
*   **Automated Privacy Risk Assessment**: Implements a logical rule engine to evaluate the sensitivity of extracted metadata. It generates a **Low, Medium, or High Risk** score based on exposed GPS coordinates, exact timestamps, and specific device identifiers.
*   **Forensics Dashboard Interface**: A modern, clean, and responsive Streamlit UI organized into logical tabs (`File Info`, `Camera Info`, `Date & Time`, `Technical Settings`, `GPS Info`).
*   **Export Capabilities**: Allows forensic investigators to generate and download detailed, structured reports in both `JSON` and `TXT` formats.
*   **Graceful Error Handling**: Built-in exception handling to manage corrupted files, unsupported formats, or images stripped of metadata gracefully without application crashes.

---

## 🛠 Technology Stack

*   **Frontend**: [Streamlit](https://streamlit.io/)
*   **Backend**: Python 3
*   **Image Processing & EXIF**: `Pillow`, `ExifRead`
*   **Data Handling**: `pandas`
*   **Map Visualization**: `folium`, `streamlit-folium`

---

## 📦 Installation & Setup (Local Development)

To run this tool locally on your machine, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/shaun6jrome/metadata-extractor.git
    cd metadata-extractor
    ```

2.  **Create a virtual environment (Recommended):**
    ```bash
    python -m venv venv
    
    # On macOS/Linux:
    source venv/bin/activate  
    
    # On Windows:
    venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Launch the application:**
    ```bash
    streamlit run app.py
    ```

---

## 🖥 Usage Guide

1.  **Upload**: Navigate to the live demo or your local server (`http://localhost:8501`) and drag-and-drop an image (`JPG`, `JPEG`, `PNG`, or `TIFF`).
2.  **Analyze**: The extraction engine will instantly parse the file and populate the dashboard.
3.  **Investigate**: Click through the detailed tabs to inspect the exact camera settings and file properties.
4.  **Visualize**: If the image contains location data, view the pinpointed location in the `GPS Info` tab.
5.  **Assess Risk**: Review the `Privacy Risk Analysis` section to understand what sensitive data the image leaks.
6.  **Export**: Click the download buttons to save your forensic report locally.

---

## 📂 Architecture & Project Structure

The project follows a clean, modular architecture separating the user interface from the core analytical logic:

```text
metadata-extractor/
│
├── app.py                     # Main Streamlit application and UI routing
├── requirements.txt           # Python dependency manifests
├── README.md                  # Project documentation
│
├── utils/                     # Core analytical modules
│   ├── exif_extractor.py      # Logic for parsing and sanitizing EXIF tags
│   ├── gps_converter.py       # Math functions for converting GPS ratios to decimals
│   ├── risk_analyzer.py       # Rule-based engine for privacy risk scoring
│   └── report_generator.py    # Formatting logic for JSON and TXT exports
```

---

## 🔒 Security & Privacy Notice
**Data Privacy:** This application is designed with security in mind. All image processing and metadata extraction occurs entirely in-memory during the runtime session. Uploaded files are **never** saved to disk or transmitted to any external servers or databases. What happens on your machine, stays on your machine.
