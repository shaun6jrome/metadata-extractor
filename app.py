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
    
    # Image Upload Section
    uploaded_file = st.file_uploader("Upload an image for analysis", type=["jpg", "jpeg", "png", "tiff"])
    
    if uploaded_file is not None:
        st.success("Image uploaded successfully!")
        
        # Display image preview and basic info in columns
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.markdown("### Image Preview")
            st.image(uploaded_file, use_container_width=True)
            
        with col2:
            st.markdown("### Basic File Information")
            # Calculate file size
            file_size_bytes = uploaded_file.size
            file_size_kb = file_size_bytes / 1024
            file_size_mb = file_size_kb / 1024
            
            if file_size_mb >= 1:
                size_str = f"{file_size_mb:.2f} MB"
            else:
                size_str = f"{file_size_kb:.2f} KB"
                
            st.info(f"**File Name:** {uploaded_file.name}")
            st.info(f"**File Type:** {uploaded_file.type}")
            st.info(f"**File Size:** {size_str}")

        st.markdown("---")
        st.markdown("## Extracted EXIF Metadata")
        
        # Extract Metadata
        from utils.exif_extractor import extract_exif_data
        
        with st.spinner('Extracting metadata...'):
            raw_metadata, parsed_data = extract_exif_data(uploaded_file)
            
        if parsed_data:
            st.markdown("### Parsed Data")
            for key, value in parsed_data.items():
                st.write(f"**{key}:** {value}")
        else:
            st.warning("No standard metadata found.")
            
        with st.expander("View Raw Metadata"):
            if raw_metadata:
                st.json(raw_metadata)
            else:
                st.write("No raw metadata could be extracted.")

    else:
        st.info("Welcome to the Metadata Extractor. Please proceed to upload an image.")

if __name__ == "__main__":
    main()
