import barcode
import db

print('=====TinStore CLI v0.1=====')
print('plese chouse and option')
print("""
\t 1 add item and print
\t 2 lookup item
\t 0 quit
""")

running = True
# opt sector
while running == True:
    option = input()

    if int(option) == 1:
        print('add item')
    elif int(option) == 2:
        print('look up item')
    elif int(option) == 0:
        print('quit bye')
        running = False
    elif int(option) == 99:
        continue
    else:
        print('not an option')
    option = 99
print(running)