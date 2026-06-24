def analyze_metadata_risk(parsed_data, gps_info):
    """
    Analyzes extracted metadata and generates a privacy risk assessment.
    Returns the risk level (Low, Medium, High) and a list of identified risks.
    """
    risk_level = "Low Risk"
    risks = []
    
    # Check for High Risk: GPS Data
    if gps_info or parsed_data.get("GPS Data Present") == "Yes":
        risk_level = "High Risk"
        risks.append("🔴 HIGH: GPS coordinates are embedded in the image. This reveals the exact location where the photo was taken.")
        
    # Check for Medium Risk: Camera Information
    if parsed_data.get("Camera Model") not in ["Unknown", "N/A"]:
        if risk_level == "Low Risk":
            risk_level = "Medium Risk"
        risks.append("🟠 MEDIUM: Camera device information is exposed. This can be used to profile the device used.")
        
    # Check for Medium Risk: Original Timestamp
    if parsed_data.get("Date Taken") not in ["Unknown", "N/A"]:
        if risk_level == "Low Risk":
            risk_level = "Medium Risk"
        risks.append("🟠 MEDIUM: Original creation timestamp is available. This reveals exactly when the photo was taken.")
        
    # Check for Low Risk: Software/Processing
    if parsed_data.get("Software") not in ["Unknown", "N/A"]:
        risks.append("🟢 LOW: Software processing information is visible.")
        
    if not risks:
        risks.append("🟢 LOW: No significant privacy risks detected. Minimal metadata found.")
        
    return risk_level, risks

def generate_forensics_summary(parsed_data, gps_info):
    """
    Generates a natural language summary of the findings.
    """
    findings = []
    if gps_info:
        findings.append("GPS coordinates")
    if parsed_data.get("Camera Model") not in ["Unknown", "N/A"]:
        findings.append("camera model information")
    if parsed_data.get("Date Taken") not in ["Unknown", "N/A"]:
        findings.append("timestamp metadata")
        
    if not findings:
        return "This image contains minimal metadata with no significant privacy risks detected."
        
    if len(findings) == 1:
        findings_str = findings[0]
    elif len(findings) == 2:
        findings_str = f"{findings[0]} and {findings[1]}"
    else:
        findings_str = f"{', '.join(findings[:-1])}, and {findings[-1]}"
        
    return f"This image contains {findings_str} which could reveal sensitive location and device details."
