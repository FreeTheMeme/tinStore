#barcode.py 
#prints prints bar

#https://labelary.com/zpl.html

import subprocess
import random
import db

def Generate_barcode(digit):
    # Generate a random nth-digit number
    barcode_number = random.randrange(10**digit-1, 10**digit)

    # if database returns nothing return barcode
    is_in_db = True
    while(is_in_db):
        if len(db.lookup_item(barcode_number)) == 0:
            print("|BC| The item is not in the database.")
            is_in_db = False
            return barcode_number
        else:
            print("|BC| The item is in the database.")

def print_barcode(barcode,name):
    printer_name = "ZD420"  # CUPS name
    # Data to send to printer
    zpl_data = """
    ^XA
    ^FO35,30
    ^AE,20,10
    ^FD"""+name+"""^FS
    ^FO35,70
    ^BY2
    ^BCN,100,Y,N,Y
    ^FD"""+str(barcode)+"""^FS
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
    ^FO35,30
    ^AE,20,10
    ^FD"""+name+"""^FS
    ^FO35,70
    ^BY2
    ^BCN,100,Y,N,Y
    ^FD"""+str(barcode)+"""^FS
    ^XZ
    """

    # Save ZPL to a temporary file
    with open("temp_label_file.zpl", "w") as f:
        f.write(zpl_data)

    # Use subprocess to send the job
    subprocess.run(["lp", "-d", printer_name, "-o", "raw", "temp_label_file.zpl"])