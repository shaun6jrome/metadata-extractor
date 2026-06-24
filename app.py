import streamlit as st

def main():
    # Set page configuration
    st.set_page_config(
        page_title="Metadata Extractor | Digital Forensics",
        page_icon="🔍",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # Custom CSS for dark forensics theme
    st.markdown("""
        <style>
        .main {
            background-color: #0e1117;
        }
        h1, h2, h3 {
            color: #00ff00 !important;
            font-family: 'Courier New', Courier, monospace;
        }
        .stButton>button {
            background-color: #00ff00;
            color: #000000;
            font-weight: bold;
            border-radius: 5px;
            border: 1px solid #00ff00;
        }
        .stButton>button:hover {
            background-color: #000000;
            color: #00ff00;
            border: 1px solid #00ff00;
        }
        </style>
    """, unsafe_allow_html=True)

    # App Header
    st.title("🔍 Metadata Extractor (EXIF Analyzer)")
    st.markdown("### Digital Forensics Image Analysis Tool")
    st.markdown("Upload an image to extract and analyze hidden metadata, GPS coordinates, and camera settings.")

    # Sidebar
    with st.sidebar:
        st.header("⚙️ Settings & Info")
        st.info("This tool extracts EXIF data from images for digital forensic analysis.")
        st.markdown("---")
        st.markdown("**Supported Formats:** JPG, JPEG, PNG, TIFF")

    # Main Content Area
    st.write("---")
    st.write("Welcome to the Metadata Extractor. Please proceed to upload an image.")

if __name__ == "__main__":
    main()
