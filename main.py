import barcode
import db

var_barc = barcode.Generate_barcode()
name = "full test"
db.insert_item(var_barc,name,"test of full system")
barcode.print_barcode(var_barc,name)
#barcode.print_barcode(barcode.Generate_barcode(),'test')
#print(db.all_items())