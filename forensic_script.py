from Registry import Registry  # Library for reading Windows registry hives

SOFTWARE_HIVE = r"C:\Users\yassi\OneDrive\Desktop\SOFTWARE"
SYSTEM_HIVE   = r"C:\Users\yassi\OneDrive\Desktop\SYSTEM"
SAM_HIVE      = r"C:\Users\yassi\OneDrive\Desktop\SAM"
NTUSER_HIVE   = r"C:\Users\yassi\OneDrive\Desktop\NTUSER.DAT"

def ts(ts):      # Convert timestamp to readable string
    return ts.strftime("%Y-%m-%d %H:%M:%S") if ts else ""  # Format as YYYY-MM-DD HH:MM:SS
