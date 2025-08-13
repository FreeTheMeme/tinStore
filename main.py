# main.py 
# applaction loop will be written here
import db
# start, the user will be promted with potions susch as:

# scan barcode lookup
items = db.lookup_item('12345')
for item in items:
    print(item[2])

# scan barcode add to db
db.insert_item('12345','coooooool-item')

# create barcode -> if yes ask to print
# view invtory
