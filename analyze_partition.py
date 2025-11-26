import struct
import os
image_path = r"C:\Users\yassi\OneDrive\Desktop\CW Disk Image\CW Image.dd"

with open(image_path, "rb") as f: 
    mbr = f.read(512)  # Read the Master Boot Record (first 512 bytes of disk)

for i in range(4):  # Loop through the 4 possible partition entries in the MBR
    entry = mbr[446 + i*16 : 446 + (i+1)*16]  # Extract each 16-byte partition entry from the MBR
    print(f"Entry {i+1}: {entry.hex()}")  # Print the raw hexadecimal representation of the partition entry
