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
        st.markdown("## Extracted EXIF Metadata Dashboard")
        
        # Extract Metadata
        from utils.exif_extractor import extract_exif_data
        from utils.gps_converter import extract_gps_data
        
        with st.spinner('Extracting metadata...'):
            raw_metadata, parsed_data, original_tags = extract_exif_data(uploaded_file)
            gps_info = extract_gps_data(original_tags)
            
        if parsed_data:
            # Create Tabs for Dashboard
            tab1, tab2, tab3, tab4, tab5 = st.tabs([
                "📁 File Info", 
                "📷 Camera Info", 
                "⏱ Date & Time", 
                "⚙️ Technical Settings",
                "📍 GPS Info"
            ])
            
            with tab1:
                st.markdown("### File Information")
                st.write(f"**Image Format:** {parsed_data.get('Image Format', 'N/A')}")
                st.write(f"**Image Mode:** {parsed_data.get('Image Mode', 'N/A')}")
                st.write(f"**Image Dimensions:** {parsed_data.get('Image Dimensions', 'N/A')}")
                
            with tab2:
                st.markdown("### Camera Information")
                st.write(f"**Camera Manufacturer:** {parsed_data.get('Camera Manufacturer', 'N/A')}")
                st.write(f"**Camera Model:** {parsed_data.get('Camera Model', 'N/A')}")
                st.write(f"**Software:** {parsed_data.get('Software', 'N/A')}")
                
            with tab3:
                st.markdown("### Date & Time Information")
                st.write(f"**Date Taken:** {parsed_data.get('Date Taken', 'N/A')}")
                st.write(f"**Date Modified:** {parsed_data.get('Date Modified', 'N/A')}")
                
            with tab4:
                st.markdown("### Technical Camera Settings")
                st.write(f"**ISO Value:** {parsed_data.get('ISO Value', 'N/A')}")
                st.write(f"**Exposure Time:** {parsed_data.get('Exposure Time', 'N/A')}")
                st.write(f"**Aperture:** {parsed_data.get('Aperture', 'N/A')}")
                st.write(f"**Focal Length:** {parsed_data.get('Focal Length', 'N/A')}")
                st.write(f"**Flash Information:** {parsed_data.get('Flash Information', 'N/A')}")
                
            with tab5:
                st.markdown("### GPS Information")
                if gps_info:
                    st.success("GPS metadata found and converted.")
                    st.write(f"**Latitude:** {gps_info['Latitude']:.6f}")
                    st.write(f"**Longitude:** {gps_info['Longitude']:.6f}")
                elif parsed_data.get("GPS Data Present") == "Yes":
                    st.warning("GPS tags exist, but could not be parsed into coordinates.")
                else:
                    st.info("No GPS metadata found in this image.")
                    
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
