import exifread
from PIL import Image
from PIL.ExifTags import TAGS

def extract_exif_data(file_bytes):
    """
    Extracts EXIF metadata from image bytes.
    Returns a dictionary of raw metadata and a parsed dictionary of common fields.
    """
    metadata = {}
    parsed_data = {}
    
    try:
        # Use ExifRead for robust tag extraction
        tags = exifread.process_file(file_bytes)
        
        # Convert values to strings for easy display
        for tag, value in tags.items():
            if tag not in ('JPEGThumbnail', 'TIFFThumbnail', 'Filename', 'EXIF MakerNote'):
                metadata[tag] = str(value)
                
        # Also try getting basic info via Pillow
        try:
            file_bytes.seek(0)
            img = Image.open(file_bytes)
            parsed_data["Image Format"] = img.format
            parsed_data["Image Mode"] = img.mode
            parsed_data["Image Dimensions"] = f"{img.width} x {img.height}"
        except Exception as e:
            parsed_data["Image Info Error"] = str(e)

        # Parse specific common fields from ExifRead tags
        parsed_data["Camera Manufacturer"] = metadata.get("Image Make", "Unknown")
        parsed_data["Camera Model"] = metadata.get("Image Model", "Unknown")
        parsed_data["Date Taken"] = metadata.get("EXIF DateTimeOriginal", "Unknown")
        parsed_data["Date Modified"] = metadata.get("Image DateTime", "Unknown")
        parsed_data["Software"] = metadata.get("Image Software", "Unknown")
        
        # Technical Camera Settings
        parsed_data["ISO Value"] = metadata.get("EXIF ISOSpeedRatings", "Unknown")
        parsed_data["Exposure Time"] = metadata.get("EXIF ExposureTime", "Unknown")
        parsed_data["Aperture"] = metadata.get("EXIF FNumber", "Unknown")
        parsed_data["Focal Length"] = metadata.get("EXIF FocalLength", "Unknown")
        parsed_data["Flash Information"] = metadata.get("EXIF Flash", "Unknown")
        
        # GPS Information flags
        gps_tags = {k: v for k, v in metadata.items() if 'GPS' in k}
        if gps_tags:
            parsed_data["GPS Data Present"] = "Yes"
        else:
            parsed_data["GPS Data Present"] = "No"

    except Exception as e:
        parsed_data["Extraction Error"] = f"Failed to extract metadata: {str(e)}"
        tags = {}

    return metadata, parsed_data, tags
