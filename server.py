from flask import Flask, jsonify, request
from flask_cors import CORS
from werkzeug import exceptions
from controllers import shoppinglist

server = Flask(__name__)
CORS(server)

@server.route('/')
def home():
    return jsonify({'message': 'Hello from Flask!'}), 200

@server.route('/list', methods=['GET', 'POST'])
def list_handler():
    fns = {
        'GET': shoppinglist.index,
        'POST': shoppinglist.create
    }
    resp, code = fns[request.method](request)
    return jsonify(resp), code

# @server.route('/list', methods=['GET', 'POST'])
# def list_handler():
#     if request.method == 'GET':
#         return jsonify({'list': shopping_list})
#     if request.method == 'POST':
#         new_item = request.get_json()
#         newitem['id'] = len(shopping_list)
#         shopping_list.append(new_item)
#         return jsonify({'list': new_item})

server.run(debug=True)