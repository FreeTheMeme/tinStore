import barcode
import db

# Function to add a barcode and corresponding name to the database.
def add_barcode():
    # Get user input for the name of the item and its barcode.
    cli_name = input('Enter name: ')
    cli_barcode = input('Scan barcode or enter manually: ')
    print(f'Adding {cli_name} \nwith barcode:{cli_barcode} ')

    # Insert the item into the database with a description of how it was added.
    db.insert_item(cli_barcode, cli_name, 'added with cli')


def lookup_barcode():
    print('Enter barcode')
    cli_barcode_l = input()
    print(db.lookup_item(cli_barcode_l))
    
# Function to generate and print a barcode using the 'Generate_barcode' function from the 'barcode' module.
def gen_and_print():
    pr_loop = True
    while pr_loop:
        cli_name = input('enter name: ')
        cli_barcode = barcode.Generate_barcode(12)

        print('barcode is: '+ str(cli_barcode))
        barcode.print_barcode(cli_barcode,cli_name)
        db.insert_item(cli_barcode,cli_name)
        ans = input('go again? Y/N')
        if ans.lower == 'n':
            print('exit')
            pr_loop = False




print('=====TinStore CLI v0.1=====')

running = True
# Option sector
while running:
    print('Please choose an option')
    print("""
    \t 1 add item 
    \t 2 lookup item
    \t 3 generate barcode and print
    \t 0 quit
    """)
    print('Enter a number')
    option = input()

    if int(option) == 1:
        print('Add item')
        add_barcode()
    elif int(option) == 2:
        print('Look up item')
        lookup_barcode()
    elif int(option) == 3:
        print('Generate and print barcode')
        gen_and_print()
    elif int(option) == 0:
        print('Quit bye')
        running = False
    elif int(option) == 99:
        continue
    else:
        print('Not an option')
    option = 99


