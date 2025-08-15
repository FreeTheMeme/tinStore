# db.py
# any data base comands will be put here
#
import mysql.connector
import texttable
#TABLES
# ============ITEMS=============
# +------------+--------------+------+-----+-------------------+-------------------+
# | Field      | Type         | Null | Key | Default           | Extra             |
# +------------+--------------+------+-----+-------------------+-------------------+
# | id         | int unsigned | NO   | PRI | NULL              | auto_increment    |
# | barcode    | varchar(50)  | NO   |     | NULL              |                   |
# | name       | varchar(255) | NO   |     | NULL              |                   |
# | date_added | datetime     | NO   |     | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
# | notes      | text         | YES  |     | NULL              |                   |
# | sold       | tinyint(1)   | NO   |     | 0                 |                   |
# +------------+--------------+------+-----+-------------------+-------------------+

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

# adds Item
def insert_item(barcode, name, notes=None, sold=False):

  sql = """
  INSERT INTO items (barcode, name, notes, sold)
  VALUES (%s, %s, %s, %s)
  """
  values = (barcode, name, notes, sold)
  mycursor.execute(sql, values)
  mydb.commit()
  print(f'|DB| added {name} to db')

# finds item
def lookup_item(barcode):

  sql = "SELECT * FROM items WHERE barcode = %s"
  mycursor.execute(sql, (barcode,))
  myresult = mycursor.fetchall()


  return myresult
# return all items
def all_items():

  sql = "SELECT * FROM items"
  mycursor.execute(sql)
  myresult = mycursor.fetchall()

  return myresult
# deletes item by barcode
def delete_item(barcode):

  sql = "DELETE FROM items WHERE barcode = %s"
  mycursor.execute(sql, (barcode,))


#im to lazy to implment this
def edit_item(barcode):
  sql = "DELETE FROM items WHERE barcode = %s"
  mycursor.execute(sql, (barcode,))