# app.py 
# applaction loop will be written here
import db
from flask import Flask
from flask import render_template

app = Flask(__name__)
headings = ("ID","barcode","name","Date Added","Notes","sold")
data = db.all_items()
@app.route("/")
def hello_world():
    return render_template('table.html',headings=headings,data=data)
