# 🔍 Metadata Extractor (EXIF Analyzer)

A complete digital forensics tool built with Python and Streamlit to extract, analyze, and display metadata from image files. This tool is designed for cybersecurity students, digital forensic investigators, photographers, and security researchers.

## 🚀 Features

- **Image Upload & Preview**: Drag and drop support for JPG, JPEG, PNG, and TIFF images.
- **EXIF Extraction Engine**: Automatically extracts embedded metadata such as Camera Manufacturer, Model, Lens Info, Date Taken, ISO, Exposure Time, and Aperture.
- **Interactive Metadata Dashboard**: Clean, organized tabs separating File Info, Camera Info, Date & Time, and Technical Settings.
- **GPS Metadata Analysis & Visualization**: Automatically converts raw GPS data into decimal degrees and plots the exact location on an interactive Folium map.
- **Privacy Risk Assessment**: Analyzes the extracted metadata to determine the privacy risk level (Low, Medium, High) based on exposed GPS coordinates, timestamps, and device identifiers.
- **Export Capabilities**: Generate and download detailed forensic reports in both JSON and TXT formats.
- **Robust Error Handling**: Gracefully handles images without EXIF data or corrupted files.

## 🛠 Technology Stack

- **Frontend**: Streamlit
- **Backend**: Python 3
- **Libraries**: 
  - `Pillow` (Image Processing)
  - `ExifRead` (Robust EXIF parsing)
  - `pandas` (Data handling)
  - `folium` & `streamlit-folium` (Map Visualization)

## 📦 Installation Guide

1. **Clone the repository:**
   ```bash
   git clone https://github.com/shaun6jrome/metadata-extractor.git
   cd metadata-extractor
   ```

2. **Create a virtual environment (Recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   streamlit run app.py
   ```

## 🖥 Usage

1. Open the application in your web browser (typically `http://localhost:8501`).
2. Use the file uploader to drag and drop an image (JPG, JPEG, PNG, or TIFF).
3. Wait for the extraction engine to process the image.
4. Navigate through the dashboard tabs to inspect the extracted data.
5. If GPS coordinates are present, view the location on the interactive map.
6. Review the **Privacy Risk Analysis** section to understand the potential exposure of the image.
7. Click the download buttons to export the findings in JSON or TXT format.

## 📂 Project Structure

```text
metadata-extractor/
│
├── app.py                     # Main Streamlit application
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
│
├── utils/                     # Utility modules
│   ├── exif_extractor.py      # EXIF parsing logic
│   ├── gps_converter.py       # GPS coordinate conversion
│   ├── risk_analyzer.py       # Privacy risk scoring logic
│   └── report_generator.py    # JSON and TXT export logic
│
├── exports/                   # Directory for saved exports (if needed locally)
└── assets/                    # Directory for static assets
```

## 🔒 Security & Privacy Notice
This tool runs entirely locally. Uploaded images are processed in-memory and are not saved or transmitted to any external servers, ensuring complete privacy during analysis.
