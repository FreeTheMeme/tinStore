import barcode
import subprocess
printer_name = "ZD420"  # CUPS name
   # Data to send to printer
zpl_data = """
^XA
^FO288,0
^AE,20,10
^FDline 1  ^FS
^FO288,30
^AE,20,10
^FDline 2^FS
^FO288,65^GB270,3,3^FS
^FO288,75
^AE,60,30
^FD BIG TEXT ^FS
^XZ
"""

    # Save ZPL to a temporary file
with open("temp_label_file.zpl", "w") as f:
        f.write(zpl_data)

    # Use subprocess to send the job
subprocess.run(["lp", "-d", printer_name, "-o", "raw", "temp_label_file.zpl"])