# db.py
# any data base comands will be put here
#
import mysql.connector
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

mycursor = mydb.cursor(dictionary=True)

# adds Item
def insert_item(item):

  sql = """
  INSERT INTO items (barcode, name, value)
  VALUES (%s, %s, %s)
  ON DUPLICATE KEY UPDATE name = %s, value = %s
  """
  values = (item['barcode'], item['name'], item['value'],item['name'], item['value'])
  mycursor.execute(sql, values)
  mydb.commit()
  print(f'|DB| added {item} to db')


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

def update_item():
  print('upadte duebug')

# deletes item by barcode
def delete_item(barcode):

  sql = "DELETE FROM items WHERE barcode = %s"
  mycursor.execute(sql, (barcode,))


#im to lazy to implment this
def edit_item(barcode):
  sql = "DELETE FROM items WHERE barcode = %s"
  mycursor.execute(sql, (barcode,))