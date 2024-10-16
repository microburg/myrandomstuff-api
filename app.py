from flask import Flask, jsonify, request

app = Flask(__name__)

myrandomstuff = []
task_id_counter = 1

@app.route('/myrandomstuff', methods=['GET'])
def get_items():
    return jsonify(myrandomstuff)

@app.route('/myrandomstuff/<int:id>', methods=['GET'])
def get_item(id):
    item = next((item for item in myrandomstuff if item['id'] == id), None)
    if item is None:
        return jsonify({'error': 'Item not found'}), 404
    return jsonify(item)

@app.route('/myrandomstuff', methods=['POST'])
def create_item():
    global task_id_counter
    new_item = {
        'id': task_id_counter,
        'title': request.json.get('title', ''),
        'completed': False
    }
    myrandomstuff.append(new_item)
    task_id_counter += 1
    return jsonify(new_item), 201

@app.route('/myrandomstuff/<int:id>', methods=['PUT'])
def update_item(id):
    item = next((item for item in myrandomstuff if item['id'] == id), None)
    if item is None:
        return jsonify({'error': 'Item not found'}), 404
    
    item['title'] = request.json.get('title', item['title'])
    item['completed'] = request.json.get('completed', item['completed'])
    return jsonify(item)

@app.route('/myrandomstuff/<int:id>', methods=['DELETE'])
def delete_item(id):
    global myrandomstuff
    myrandomstuff = [item for item in myrandomstuff if item['id'] != id]
    return jsonify({'message': 'Item deleted'})

if __name__ == '__main__':
    app.run(debug=True)
