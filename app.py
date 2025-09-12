# app.py 
# endpoints for API
import db
import barcode
from flask import Flask
# from flask import render_template
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

# Create a new item.
@app.route('/items', methods=['POST'])
def create_item():
    # request.json contains the JSON data sent with the POST request.
    print(f"Request: {request.form}")
    item_data = jsonify(request.form).json
    print(f"Item data: {item_data}")
    db.insert_item(item_data)
    return "OK"

    # Return a JSON response with the newly created item and a 201 status code (Created).
    #return jsonify({'item': item_data}), 201

#Retrieve the list of all items.
@app.route('/items', methods=['GET'])
def get_items():

    # jsonify is a Flask helper that converts a Python dictionary to a JSON response.
    return jsonify({'items': db.all_items()})

# GET a single item by ID
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    # Endpoint to retrieve a single item by its ID.
    return jsonify({'item': db.lookup_item(item_id)})

# Update an existing item by ID
@app.route('/items/<int:item_id>', methods=['POST'])
def update_item(item_id):
    db.update_item(item_id)

# DELETE a item by ID
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    db.delete_item(item_id)

    return jsonify({'result': True, 'message': f'item with ID {item_id} has been deleted.'})

# # print lable for item
# @app.route('/print/<int:item_id>', methods=['GET'])
# def print(item_id):
#     item = db.lookup_item(item_id)
#     # pick first item in list (aka 0th)
#     barcode_var = item[0]['barcode']
#     name = item[0]['name']
#     barcode.print_barcode(barcode_var,name)
#     return jsonify({'msg':'printed'})



# --- Run the Application ---
# The __name__ == '__main__' block ensures that this code runs only when the script
# is executed directly (not when it's imported as a module).
if __name__ == '__main__':
    # app.run() starts the Flask development server.
    # debug=True enables debug mode, which provides helpful error messages
    # and automatically reloads the server when you make changes.
    app.run(debug=True, host='0.0.0.0')
