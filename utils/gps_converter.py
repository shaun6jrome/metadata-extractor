def get_if_exist(data, key):
    if key in data:
        return data[key]
    return None

def convert_to_degrees(value):
    """
    Helper function to convert the GPS coordinates stored in the EXIF to degrees in float format.
    EXIF stores GPS coordinates as a ratio.
    """
    try:
        d = float(value.values[0].num) / float(value.values[0].den)
        m = float(value.values[1].num) / float(value.values[1].den)
        s = float(value.values[2].num) / float(value.values[2].den)
        return d + (m / 60.0) + (s / 3600.0)
    except Exception:
        return None

def extract_gps_data(raw_metadata):
    """
    Extracts and converts GPS data from raw EXIF metadata into decimal degrees.
    """
    gps_info = {}
    
    gps_latitude = get_if_exist(raw_metadata, 'GPS GPSLatitude')
    gps_latitude_ref = get_if_exist(raw_metadata, 'GPS GPSLatitudeRef')
    gps_longitude = get_if_exist(raw_metadata, 'GPS GPSLongitude')
    gps_longitude_ref = get_if_exist(raw_metadata, 'GPS GPSLongitudeRef')

    if gps_latitude and gps_latitude_ref and gps_longitude and gps_longitude_ref:
        lat = convert_to_degrees(gps_latitude)
        if lat is None:
            return None
        
        if gps_latitude_ref.values[0] != 'N':
            lat = -lat

        lon = convert_to_degrees(gps_longitude)
        if lon is None:
            return None
            
        if gps_longitude_ref.values[0] != 'E':
            lon = -lon
            
        gps_info['Latitude'] = lat
        gps_info['Longitude'] = lon
        return gps_info
        
    return None
