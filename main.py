import barcode
import db



def add_barcode():
    print('enter name:')
    cli_name = input()
    print('scan barcode or enter manuly')
    cli_barcode = input()
    print(f'adding {cli_name} \nwith barcode:{cli_barcode} ')
    db.insert_item(cli_barcode,cli_name,'added with cli')
    print('print y/n')
def lookup_barcode():
    print('enter barcode')
    cli_barcode_l = input()
    print(db.lookup_item())



print('=====TinStore CLI v0.1=====')

running = True
# opt sector
while running == True:
    print('plese chouse and option')
    print("""
    \t 1 add item and print
    \t 2 lookup item
    \t 0 quit
    """)
    print('enter a number')
    option = input()

    if int(option) == 1:
        print('add item')
        add_barcode()
    elif int(option) == 2:
        print('look up item')
        lookup_barcode()
    elif int(option) == 0:
        print('quit bye')
        running = False
    elif int(option) == 99:
        continue
    else:
        print('not an option')
    option = 99
print(running)

