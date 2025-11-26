import struct
import os
image_path = r"C:\Users\yassi\OneDrive\Desktop\CW Disk Image\CW Image.dd"

with open(image_path, "rb") as f: 
    mbr = f.read(512)  # Read the Master Boot Record (first 512 bytes of disk)

for i in range(4):  # Loop through the 4 possible partition entries in the MBR
    entry = mbr[446 + i*16 : 446 + (i+1)*16]  # Extract each 16-byte partition entry from the MBR
    print(f"Entry {i+1}: {entry.hex()}")  # Print the raw hexadecimal representation of the partition entry

print("\n=== DECODED PARTITION TABLE ===")

for i in range(4):  # Loop through the 4 partition entries again for detailed decoding
    entry = mbr[446 + i*16 : 446 + (i+1)*16]   # Extract each 16-byte partition entry from the MBR

    # Unpack MBR entry into its fields
    boot_flag, start_chs, ptype, end_chs, start_sector, num_sectors = struct.unpack(  
        "<B3sB3sII", entry
    )

    size_bytes = num_sectors * 512   # Calculate partition size in bytes (sectors * bytes per sector)
    size_mb = round(size_bytes / (1024 * 1024), 2)   # Convert bytes to megabytes and round to 2 decimal places
    size_gb = round(size_bytes / (1024 * 1024 * 1024), 2)  # Convert bytes to gigabytes and round to 2 decimal places

    print(f"\nPartition {i+1}")  
    print("------------------------")
    print("Type:", hex(ptype))  
    print("Start Sector:", start_sector)  
    print("Number of Sectors:", num_sectors)  
    print(f"Size: {size_bytes} bytes | {size_mb} MB | {size_gb} GB")  
