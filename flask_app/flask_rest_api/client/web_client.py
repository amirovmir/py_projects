import requests

r = requests.get('http://127.0.0.1:5000/users')
print(r.status_code, r.headers, r.text, r.json())

r = requests.post('http://127.0.0.1:5000/users', json={"name": "Peter", "surname": "Green"})
print(r.json())

r = requests.put('http://127.0.0.1:5000/users', json={"id": "1", "name": "Mark", "surname": "Brown"})
print(r.json())

r = requests.delete('http://127.0.0.1:5000/users', json={"id": "1"})
print(r.json())