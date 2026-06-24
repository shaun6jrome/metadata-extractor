import json

def generate_json_report(parsed_data, gps_info, risk_level, risks):
    """
    Generates a JSON string of the extracted metadata and risk assessment.
    """
    report_dict = {
        "metadata": parsed_data,
        "gps_info": gps_info if gps_info else "None",
        "risk_assessment": {
            "level": risk_level,
            "details": risks
        }
    }
    return json.dumps(report_dict, indent=4)

def generate_txt_report(parsed_data, gps_info, risk_level, risks):
    """
    Generates a formatted text report of the extracted metadata and risk assessment.
    """
    report_lines = []
    
    report_lines.append("="*50)
    report_lines.append("METADATA FORENSICS REPORT")
    report_lines.append("="*50)
    report_lines.append("\n[FILE INFORMATION]")
    
    for key in ["Image Format", "Image Mode", "Image Dimensions"]:
        report_lines.append(f"{key}: {parsed_data.get(key, 'N/A')}")
        
    report_lines.append("\n[CAMERA INFORMATION]")
    for key in ["Camera Manufacturer", "Camera Model", "Software"]:
        report_lines.append(f"{key}: {parsed_data.get(key, 'N/A')}")
        
    report_lines.append("\n[DATE & TIME INFORMATION]")
    for key in ["Date Taken", "Date Modified"]:
        report_lines.append(f"{key}: {parsed_data.get(key, 'N/A')}")
        
    report_lines.append("\n[TECHNICAL SETTINGS]")
    for key in ["ISO Value", "Exposure Time", "Aperture", "Focal Length", "Flash Information"]:
        report_lines.append(f"{key}: {parsed_data.get(key, 'N/A')}")
        
    report_lines.append("\n[GPS INFORMATION]")
    if gps_info:
        report_lines.append(f"Latitude: {gps_info['Latitude']:.6f}")
        report_lines.append(f"Longitude: {gps_info['Longitude']:.6f}")
    else:
        report_lines.append("No GPS metadata found.")
        
    report_lines.append("\n[PRIVACY RISK ASSESSMENT]")
    report_lines.append(f"Overall Risk Level: {risk_level}")
    for risk in risks:
        report_lines.append(risk)
        
    report_lines.append("\n" + "="*50)
    report_lines.append("END OF REPORT")
    report_lines.append("="*50)
    
    return "\n".join(report_lines)
