# app.py 
# applaction loop will be written here
import db
from flask import Flask
from flask import render_template

# main.py
# Import necessary modules from the Flask framework
from flask import Flask, jsonify, request

# Create an instance of the Flask class. 
# __name__ is a special Python variable that gets the name of the current module.
# This is needed so Flask knows where to look for resources like templates and static files.
app = Flask(__name__)



# --- API Endpoints (Routes) ---

# This decorator turns a regular Python function into a Flask view function.
# It maps the URL endpoint '/' to the index() function.
@app.route('/', methods=['GET'])
def index():
    return jsonify({'message': 'Welcome to the Flask REST API!'})

    # Endpoint to retrieve the list of all items.

@app.route('/items', methods=['GET'])
def get_items():

    # jsonify is a Flask helper that converts a Python dictionary to a JSON response.
    return jsonify({'items': db.all_items()})

# GET a single item by ID
@app.route('/items/<string:item_id>', methods=['GET'])
def get_item(item_id):
    # Endpoint to retrieve a single item by its ID.
    return jsonify({'item': db.lookup_item(item_id)})



# DELETE a item
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    db.delete_item(item_id)

    return jsonify({'result': True, 'message': f'item with ID {item_id} has been deleted.'})

# print lable for item
@app.route('/print<int:item_id>', methods=['GET'])
def index():
    return jsonify({'message': 'Printed'})



# --- Run the Application ---
# The __name__ == '__main__' block ensures that this code runs only when the script
# is executed directly (not when it's imported as a module).
if __name__ == '__main__':
    # app.run() starts the Flask development server.
    # debug=True enables debug mode, which provides helpful error messages
    # and automatically reloads the server when you make changes.
    app.run(debug=True)
