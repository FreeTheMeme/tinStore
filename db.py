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

mycursor.execute("CREATE TABLE IF NOT EXISTS players (name VARCHAR(255), uuid VARCHAR(255), time_played INT(11))")     

def insert_item(barcode, name, notes=None, sold=False):

  sql = """
  INSERT INTO items (barcode, name, notes, sold)
  VALUES (%s, %s, %s, %s)
  """
  values = (barcode, name, notes, sold)
  mycursor.execute(sql, values)
  mydb.commit()
  print(f'|DB| added {name} to db')