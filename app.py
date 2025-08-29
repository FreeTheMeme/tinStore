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
    """A simple welcome route to test if the server is running."""
    return jsonify({'message': 'Welcome to the Flask REST API!'})

# GET all items
@app.route('/items', methods=['GET'])
def get_items():
    """
    Endpoint to retrieve the list of all items.
    HTTP Method: GET
    URL: /items
    """
    # jsonify is a Flask helper that converts a Python dictionary to a JSON response.
    return jsonify({'items': db.all_items()})

# GET a single item by ID
@app.route('/items/<string:item_id>', methods=['GET'])
def get_item(item_id):
    """
    Endpoint to retrieve a single item by its ID.
    HTTP Method: GET
    URL: /items/<item_id> (e.g., /items/1)
    """
    # if item is None:
    #     # If the item is not found, return a 404 error with a custom message.
    #     return jsonify({'error': 'item not found'}), 404
    return jsonify({'item': db.lookup_item(item_id)})

# POST (Create) a new item
@app.route('/items', methods=['POST'])
def create_item():
    """
    Endpoint to create a new item.
    HTTP Method: POST
    URL: /items
    Request Body (JSON): {"title": "New item Title", "description": "Optional description"}
    """
    # Check if the request contains JSON data and a 'title' field.
    if not request.json or not 'title' in request.json:
        return jsonify({'error': 'Missing title in request body'}), 400

    # Create a new item dictionary.
    new_item = {
        'id': items[-1]['id'] + 1 if items else 1, # Simple ID generation
        'title': request.json['title'],
        'description': request.json.get('description', ""), # Optional field
        'done': False
    }
    items.append(new_item)
    
    # Return the newly created item with a 201 Created status code.
    return jsonify({'item': new_item}), 201

# PUT (Update) an existing item
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    """
    Endpoint to update an existing item.
    HTTP Method: PUT
    URL: /items/<item_id>
    Request Body (JSON): {"title": "Updated Title", "description": "Updated Desc", "done": true}
    """
    item = find_item(item_id)
    if item is None:
        return jsonify({'error': 'item not found'}), 404
    
    # Ensure the request contains JSON data.
    if not request.json:
        return jsonify({'error': 'Invalid request'}), 400

    # Update fields if they are provided in the request body.
    item['title'] = request.json.get('title', item['title'])
    item['description'] = request.json.get('description', item['description'])
    item['done'] = request.json.get('done', item['done'])
    
    return jsonify({'item': item})

# DELETE a item
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    """
    Endpoint to delete a item.
    HTTP Method: DELETE
    URL: /items/<item_id>
    """
    item = find_item(item_id)
    if item is None:
        return jsonify({'error': 'item not found'}), 404
        
    items.remove(item)
    return jsonify({'result': True, 'message': f'item with ID {item_id} has been deleted.'})

# --- Run the Application ---
# The __name__ == '__main__' block ensures that this code runs only when the script
# is executed directly (not when it's imported as a module).
if __name__ == '__main__':
    # app.run() starts the Flask development server.
    # debug=True enables debug mode, which provides helpful error messages
    # and automatically reloads the server when you make changes.
    app.run(debug=True)
