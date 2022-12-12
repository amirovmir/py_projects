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

@app.route('/users', methods=['DELETE'])
def del_user():
    for user in data:
        if user['id'] == request.get_json()['id']:
            data.remove(user)
    return jsonify(data)

@app.route('/users', methods=['PUT'])
def update_user():
    for user in data:
        if user['id'] == request.get_json()['id']:
            user['name'] = request.get_json()['name'],
            user['surname'] = request.get_json()['surname']
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)

