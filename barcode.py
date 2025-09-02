#barcode.py 
#prints prints bar

#https://labelary.com/zpl.html

import subprocess
import random
import db

def Generate_barcode():
    # Generate a random nth-digit number
    barcode_number = random.randrange(10**7, 10**8)
    return barcode_number


def print_barcode(barcode,name):
    printer_name = "ZD420"  # CUPS name
    # Data to send to printer
    zpl_data = """
    ^XA
    ^FO288,0
    ^AE,20,10
    ^FD"""+name+"""^FS
    ^FO288,45
    ^FO288,50^BQN,2,5^FD"""+str(barcode)+"""^FS
    ^XZ
    """

    # Save ZPL to a temporary file
    with open("temp_label_file.zpl", "w") as f:
        f.write(zpl_data)
        f.flush()

    # Use subprocess to send the job
    subprocess.run(["lp", "-d", printer_name, "-o", "raw", "temp_label_file.zpl"])


def print_barcode_1_5in(barcode,name):
    printer_name = "ZD420"  # CUPS name
    # Data to send to printer
    zpl_data = """
    ^XA
    ^FO10,30
    ^AE,30,15
    ^FD"""+name+"""^FS
    ^FO10,70
    ^BY2
    ^BCN,100,Y,N,Y
    ^FD"""+str(barcode)+"""^FS
    ^FO200,60^BQN,2,4^FDQ,"""+str(barcode)+"""^FS 
    ^XZ
    """

    # Save ZPL to a temporary file
    with open("temp_label_file.zpl", "w") as f:
        f.write(zpl_data)

    # Use subprocess to send the job
    subprocess.run(["lp", "-d", printer_name, "-o", "raw", "temp_label_file.zpl"])