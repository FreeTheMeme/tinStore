# db.py
# any data base comands will be put here
#
import mysql.connector
#TABLES
    # item table 
    # barcode id or just id
    # name
    # date added
    # notes
    # sold bool

    # users table (probly won't be implmented till later)
    # name 
    # rank
    # password (hased)

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="example",
  database="tinstore",
)

mycursor = mydb.cursor()

#adds Item
def insert_item(barcode, name, notes=None, sold=False):

  sql = """
  INSERT INTO items (barcode, name, notes, sold)
  VALUES (%s, %s, %s, %s)
  """
  values = (barcode, name, notes, sold)
  mycursor.execute(sql, values)
  mydb.commit()
  print(f'|DB| added {name} to db')
#finds item
def lookup_item(barcode):

  sql = "SELECT * FROM items WHERE barcode = %s"
  mycursor.execute(sql, (barcode,))
  myresult = mycursor.fetchall()

  #remove tuples
  pl = list(sum(myresult, ()))
  return myresult