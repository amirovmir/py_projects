import json
from flask import Flask, jsonify, request, abort
app = Flask(__name__)

data = [{'id': '0', 'name': 'Alex', 'surname': 'Turner'},
        {'id': '1', 'name': 'Thom', 'surname': 'Yorke'}]

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(data)

@app.route('/users', methods=['POST'])
def add_user():
    req_data = {
        'id': int(data[-1]['id']) + 1,
        'name': request.json['name'],
        'surname': request.json['surname']
    }
    data.append(req_data)
    return jsonify(data)

@app.route('/users/<int:id>', methods=['DELETE'])
def del_user(id):
    del_data = data[id]
    data.pop(del_data)
    return jsonify({'result': True})

@app.route('/users/<int:id>', methods=['PUT'])
def update_user():
    data.filter(data['id'] == request.json.get('id'))
    data[0]['name'] = request.json.get('name')
    data[0]['surname'] = request.json.get('surname')
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)

