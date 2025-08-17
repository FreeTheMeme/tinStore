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
    print(db.lookup_item(cli_barcode_l))
def gen_and_print():
    print('generate and print barcode')


print('=====TinStore CLI v0.1=====')

running = True
# opt sector
while running:
    print('plese chouse and option')
    print("""
    \t 1 add item 
    \t 2 lookup item
    \t 3 generate barcode and print
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
    elif int(option) == 3:
        print('generate and print barcode')
        gen_and_print()
    elif int(option) == 0:
        print('quit bye')
        running = False
    elif int(option) == 99:
        continue
    else:
        print('not an option')
    option = 99

