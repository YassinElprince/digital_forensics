from Registry import Registry  # Library for reading Windows registry hives

SOFTWARE_HIVE = r"C:\Users\yassi\OneDrive\Desktop\SOFTWARE"
SYSTEM_HIVE   = r"C:\Users\yassi\OneDrive\Desktop\SYSTEM"
SAM_HIVE      = r"C:\Users\yassi\OneDrive\Desktop\SAM"
NTUSER_HIVE   = r"C:\Users\yassi\OneDrive\Desktop\NTUSER.DAT"

def ts(ts):      # Convert timestamp to readable string
    return ts.strftime("%Y-%m-%d %H:%M:%S") if ts else ""  # Format as YYYY-MM-DD HH:MM:SS

def installed_apps(software):
    print("\n=== INSTALLED APPLICATIONS ===")
    paths = [
        r"Microsoft\Windows\CurrentVersion\Uninstall",              # 64-bit uninstall path
        r"Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall",  # 32-bit uninstall path
    ]

    for p in paths:                                               # Iterate through both registry uninstall paths
        key = software.open(p)                                    # Open uninstall key
        for sub in key.subkeys():                                 # Loop through installed program entries
            values = {v.name(): v.value() for v in sub.values()}  # Store values in dict
            if not values.get("DisplayName"):                     # Skip entries without a program name
                continue

            print(f"- {values.get('DisplayName')} "               
                  f"| Version: {values.get('DisplayVersion')} "  
                  f"| Publisher: {values.get('Publisher')}")     
