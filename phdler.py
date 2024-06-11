from flask import Flask, jsonify, request
from functions import *  # Import your custom functions

app = Flask(__name__)

# This works
@app.route('/start', methods=['POST'])
def start():
    try:
        dl_start()
        return jsonify({"message": "Download started successfully."}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/custom', methods=['POST'])
def custom():
    item = requests.json.get('item')
    if not item:
        return jsonify({"error": "Missing item parameter."}), 400
    try:
        custom_dl(item)
        return jsonify({"message": "Custom download started successfully."}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# This works 
@app.route('/add', methods=['POST'])
def add():
    recived = request.json
    print(recived.get('item'))
    item = recived.get('item')
    if not item:
        return jsonify({"error": "Missing item parameter."}), 400
    try:
        add_check(item)
        return jsonify({"message": "Item added successfully."}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/delete', methods=['DELETE'])
def delete():
    item_type = request.json.get('type')
    item_id = request.json.get('id')
    if not item_type:
        return jsonify({"error": "Missing type parameter."}), 400
    if not item_id:
        return jsonify({"error": "Missing id parameter."}), 400
    try:
        type_check(item_type)
        delete_item(item_id)
        return jsonify({"message": "Item deleted successfully."}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/list', methods=['POST'])
def list_item():

    recived = request.json
    print(recived.get('item'))
    item_type = recived.get('item')

    if not item_type:
        return jsonify({"error": "Missing type parameter."}), 400
    try:
        type_check(item_type)
        list_items(item_type)
        return jsonify({"items": list_items(item_type)}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/help', methods=['GET'])
def help():
    try:
        help_text = help_command()
        return jsonify({"help": help_text}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"error": "Command not found!"}), 404

@app.route('/')
def index():
    return jsonify({"error": "Missing command."}), 400

if __name__ == '__main__':
    check_for_database()
    app.run(host='0.0.0.0', port=5000)

