import psycopg2
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="123",
    port="5432"
)
cursor = conn.cursor()

success_message = {'success': True}

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/users/', methods=['GET'])
def get_users():
    user_data = []
    sql = 'SELECT * FROM main;'
    cursor.execute(sql)
    data = cursor.fetchall()
    for user in data:
        user_data.append({'id': user[0],
                          'name': user[1],
                          'surname': user[2],
                          'phone number': user[3]})
    return render_template('users.html', users=user_data)

@app.route('/users/<userid>', methods=['GET'])
def get_user(userid):
    user_data = []
    sql = 'SELECT * FROM main WHERE main_id = %s'
    cursor.execute(sql, (str(userid),) )
    data = cursor.fetchall()
    for user in data:
        user_data.append({'id': user[0],
                            'name': user[1],
                            'surname': user[2],
                            'phone number': user[3]})
    return render_template('user.html', user=user_data)

@app.route('/users/', methods=['POST'])
def add_user():
    sql = 'INSERT INTO main (name, surname, telephone) VALUES (%s, %s, %s)'
    name = request.json['name']
    surname = request.json['surname']
    tel = request.json['tel']
    cursor.execute(sql, (name, surname, tel))
    conn.commit()
    return get_users()

@app.route('/users/<userid>', methods=['DELETE'])
def del_user(userid):
    sql = 'DELETE FROM main WHERE main_id = %s'
    cursor.execute(sql, (str(userid),))
    conn.commit()
    return get_users()

@app.route('/users/<userid>', methods=['PUT'])
def update_user(userid):
    sql = 'UPDATE main SET name = %s, surname = %s, telephone = %s WHERE main_id = %s'
    name = request.json['name']
    surname = request.json['surname']
    tel = request.json['tel']
    cursor.execute(sql, (name, surname, tel, str(userid)))
    conn.commit()
    return get_user(userid)


if __name__ == '__main__':
    app.run(debug=True)

