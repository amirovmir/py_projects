import psycopg2
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="123"
)
cursor = conn.cursor()

success_message = {'success': True}

@app.route('/users/', methods=['GET'])
def get_users():
    sql = 'SELECT * FROM main;'
    cursor.execute(sql)
    data = cursor.fetchall()
    print(data)
    return data

@app.route('/users/<userid>', methods=['GET'])
def get_user(userid):
    sql = 'SELECT * FROM main WHERE main_id = %s'
    cursor.execute(sql, (str(userid),) )
    data = cursor.fetchall()
    print(data)
    return data

@app.route('/users/', methods=['POST'])
def add_user():
    sql = 'INSERT INTO main (name, surname, telephone) VALUES (%s, %s, %s)'
    name = request.json['name']
    surname = request.json['surname']
    tel = request.json['tel']
    cursor.execute(sql, (name, surname, tel))

@app.route('/users/<userid>', methods=['DELETE'])
def del_user(userid):
    sql = 'DELETE FROM main WHERE main_id = %s'
    cursor.execute(sql, (str(userid),))
    data = cursor.fetchall()

@app.route('/users/<userid>', methods=['PUT'])
def update_user(userid):
    sql = 'UPDATE main SET name = %s, surname = %s, telephone = %s WHERE main_id = %s'
    name = request.json['name']
    surname = request.json['surname']
    tel = request.json['tel']
    cursor.execute(sql, (name, surname, tel, str(userid)))


if __name__ == '__main__':
    app.run(debug=True)
