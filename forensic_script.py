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

def user_accounts(sam):
    print("\n=== USER ACCOUNTS ===")             
    key = sam.open(r"SAM\Domains\Account\Users\Names")       # Registry path to local users
    for sub in key.subkeys():                                # Loop through usernames
        print(f"- Username: {sub.name()} "                   # Print username
              f"| LastWrite: {ts(sub.timestamp())}")         # Last modification time

def usb_history(system):
    print("\n=== USB HISTORY ===")                
    select = system.open("Select").value("Current").value()       # Identify current control set
    cs = f"ControlSet00{select}"                                  # Format control set name           
    for p in [rf"{cs}\Enum\USBSTOR", rf"{cs}\Enum\USB"]:          # USB connection registry paths
        key = system.open(p)                                      # Open USB registry key
        for dev in key.subkeys():                                 # Loop USB device classes
            for inst in dev.subkeys():                            # Loop device instances
                print(f"- Device ID: {inst.name()} "              # Print device instance ID (serial)
                      f"| LastWrite: {ts(inst.timestamp())}")     # Timestamp last seen

def main():     
    installed_apps(Registry.Registry(SOFTWARE_HIVE))  
    user_accounts(Registry.Registry(SAM_HIVE))        
    usb_history(Registry.Registry(SYSTEM_HIVE))      

if __name__ == "__main__":
    main()                                        
